# Image to Word

Convert scanned JPG or PNG images into editable Word documents using OCR. This Flask prototype combines Tesseract text recognition with basic paragraph and formatting heuristics.

## Features

- Upload an image through a simple web form.
- Extract text and generate a downloadable `.docx` file.
- Attempt to preserve basic paragraph structure, alignment, bold, and italic styling.

## Stack

Python · Flask · Tesseract OCR · OpenCV · Pillow · python-docx

## Run locally

Install Tesseract OCR and make sure the `tesseract` command is available on your PATH. Then, from the repository root:

```bash
python -m venv .venv
```

Activate the environment:

```powershell
# Windows PowerShell
.venv\\Scripts\\Activate.ps1
```

```bash
# macOS / Linux
source .venv/bin/activate
```

Install dependencies and start the app:

```bash
pip install -r requirements.txt
python app.py
```

Open `http://127.0.0.1:5000/`, choose a clear JPG or PNG scan, and select **Convert**. The response downloads as `converted.docx`.

## How it works

1. Flask receives the image at `POST /convert`.
2. `ocr_utils.py` processes the image and builds a Word document.
3. The browser receives the generated file as a download.

## Repository layout

| Path | Purpose |
| --- | --- |
| `app.py` | Upload form, conversion route, and download response |
| `ocr_utils.py` | OCR and document generation |
| `static/` | Interface styles |
| `requirements.txt` | Python dependencies |
| `Procfile`, `render.yaml`, `nixpacks.toml`, `Aptfile` | Deployment configuration files |

## Limitations

Formatting is estimated, not reconstructed exactly. Clear single-column scans are the intended starting point; complex layouts and poor-quality images may need manual correction. Review extracted text before using the document.

The development entry point binds to all interfaces with debug mode enabled. Public deployment needs upload validation, request-size limits, temporary-file cleanup, and production configuration. Included deployment files are not evidence of a verified live deployment.
