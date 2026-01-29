# Image → Word Converter (MVP)

This project is a minimal prototype that converts a scanned document or image (JPG/PNG) into a formatted `.docx` file. It preserves basic paragraph structure and attempts simple detection of bold and italic text plus alignment heuristics.

Quick start

1. Install system dependency: Tesseract OCR must be installed on your machine and available on PATH. On Windows install from: https://github.com/tesseract-ocr/tesseract
2. Create a virtualenv and install Python packages:

```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

3. Run the Flask app:

```bash
python app.py
```

4. Open http://127.0.0.1:5000/ and upload an image.

Notes and limitations
- Bold/italic detection is heuristic-based (image stroke density and orientation). It works for clear, single-column documents but will not be perfect.
- For production-quality formatting retainment, a richer OCR + layout analysis pipeline is recommended.
