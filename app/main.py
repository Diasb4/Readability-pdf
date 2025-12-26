from fastapi import FastAPI, UploadFile, File, HTTPException

app = FastAPI(title="PDF Readability Checker")

@app.post("/check_readability")
async def check_readability(file: UploadFile = File(...)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="File must be a PDF")

    pdf_bytes = await file.read()
    text = extract_text_from_pdf(pdf_bytes)

    readable = is_readable(text)

    return {
        "readable": readable
    }
