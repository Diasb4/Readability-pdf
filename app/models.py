from pydantic import BaseModel
from typing import Optional

class ReadabilityJobResponse(BaseModel):
    id: str
    status: str

class ReadabilityProcessingResponse(BaseModel):
    id: str
    status: str

class ReadabilityCompletedResponse(BaseModel):
    id: str
    status: str
    readable: bool
    flesch_score: Optional[float] = None
    avg_sentence_length: Optional[float] = None
    avg_word_length: Optional[float] = None
    score: Optional[int] = None
    reason: Optional[str] = None
