
````markdown
# PDF Readability Assessor

This project provides a service to assess the readability of PDF documents. It calculates metrics such as Flesch Reading Ease, average sentence length, and average word length. The service can be run locally using Docker.

---

## GitHub Repository

[Readability-pdf](https://github.com/Diasb4/Readability-pdf)

---

## Features

- Detects whether a PDF is readable by the system.
- Computes **Flesch Reading Ease** score.
- Calculates average sentence and word lengths.
- Returns a structured JSON response.

Example response:
```json
{
  "id": "1302e3ac-6c68-47d0-b060-33a282d08635",
  "status": "completed",
  "readable": true,
  "flesch_score": -8.88,
  "avg_sentence_length": 36.76,
  "avg_word_length": 6.53,
  "score": 3,
  "reason": null
}
````

---

## Prerequisites

* [Docker](https://www.docker.com/get-started) installed on your system.
* Git (optional, for cloning the repo).

---

## Docker Commands

### 1. Build the Docker image

```bash
docker build -t pdf-readability .
```

### 2. Run the Docker container

```bash
docker run -p 8000:8000 pdf-readability
```

* This starts the server and exposes it on `http://localhost:8000`.

---

## Setup without Docker (Optional)

If you want to run locally without Docker:

```bash
git clone https://github.com/Diasb4/Readability-pdf.git
cd Readability-pdf
# install dependencies (example: pip install -r requirements.txt)
# run the server (example: python main.py)
```

---

## Usage

* Send a PDF to the service endpoint (e.g., via `POST /upload`) to get a readability assessment.
* The service returns a JSON response with readability metrics.

### Example with `curl`

```bash
curl -X POST -F "file=@sample.pdf" http://localhost:8000/upload
```

---

## Notes

* The service uses automated metrics to determine readability. A negative Flesch score indicates very complex or dense text.
* Docker ensures a consistent environment across machines.

---

