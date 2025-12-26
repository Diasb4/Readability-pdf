from fastapi import FastAPI, UploadFile, File, HTTPException, BackgroundTasks
from typing import Union
import tempfile

from app.storage.memory import save_result, get_result
from app.tasks.readability_task import run_readability_task
from app.models import (
    ReadabilityJobResponse,
    ReadabilityProcessingResponse,
    ReadabilityCompletedResponse
)

app = FastAPI(title="PDF Readability Service", version="1.0.0")

@app.get("/")
def health_check():
    return {"status": "ok"}

@app.post("/readability", response_model=ReadabilityJobResponse)
async def check_readability(
    background_tasks: BackgroundTasks,
    file: UploadFile = File(...)
):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="PDF only")

    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(await file.read())
        pdf_path = tmp.name

    result_id = save_result({"status": "processing"})

    background_tasks.add_task(
        run_readability_task,
        result_id,
        pdf_path
    )

    return ReadabilityJobResponse(
        id=result_id,
        status="processing"
    )

@app.get(
    "/readability/result/{result_id}",
    response_model=Union[
        ReadabilityProcessingResponse,
        ReadabilityCompletedResponse
    ]
)
def get_readability_result(result_id: str):
    result = get_result(result_id)
    if not result:
        raise HTTPException(status_code=404, detail="Result not found")

    if result["status"] == "processing":
        return ReadabilityProcessingResponse(
            id=result_id,
            status="processing"
        )

    return ReadabilityCompletedResponse(
    id=result_id,
    status="completed",
    readable=result["readable"],
    flesch_score=result.get("flesch_score"),
    avg_sentence_length=result.get("avg_sentence_length"),
    avg_word_length=result.get("avg_word_length"),
    score=result.get("score"),
    reason=result.get("reason")
)

