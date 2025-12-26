import fitz
import textstat
import time
from app.storage.memory import update_result

def extract_text(pdf_path: str) -> str:
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def run_readability_task(result_id: str, pdf_path: str):
    start = time.time()

    text = extract_text(pdf_path)

    if not text or len(text) < 200:
        update_result(result_id, {
            "status": "completed",
            "readable": False,
            "reason": "no_text",
            "duration_seconds": time.time() - start
        })
        return

    flesch = textstat.flesch_reading_ease(text)
    avg_sentence = textstat.avg_sentence_length(text)
    avg_word = textstat.avg_letter_per_word(text)

    score = 0

    # Text exists
    score += 1

    # Flesch: allow technical docs
    if flesch >= 20:
        score += 1

    # Sentence length: be tolerant of PDF mess
    if avg_sentence <= 45:
        score += 1

    # Word length: very weak signal
    if avg_word <= 7:
        score += 1

    readable = score >= 3

    update_result(result_id, {
        "status": "completed",
        "readable": readable,
        "flesch_score": flesch,
        "avg_sentence_length": avg_sentence,
        "avg_word_length": avg_word,
        "score": score,
        "duration_seconds": time.time() - start
    })
