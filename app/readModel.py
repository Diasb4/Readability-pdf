import fitz  # PyMuPDF
import textstat

def extract_text_from_pdf(pdf_bytes: bytes) -> str:
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text.strip()

def is_readable(text: str) -> bool:
    if not text or len(text) < 300:
        return False

    flesch_score = textstat.flesch_reading_ease(text)
    avg_sentence_length = textstat.avg_sentence_length(text)
    avg_word_length = textstat.avg_letter_per_word(text)

    if flesch_score < 40:
        return False
    if avg_sentence_length > 35:
        return False
    if avg_word_length > 6:
        return False

    return True
