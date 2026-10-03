# V12 AI Security Detection Project

This project is a Flask-based AI security screening application designed to examine uploaded images and user prompts before sending them to a Gemini-powered model. It combines OCR, pattern matching, semantic analysis, and steganography checks to flag suspicious or malicious content.

## Project Purpose

The app is intended to act as a safety layer for an AI chat system. It checks whether the input appears to be:

- a malicious prompt injection
- a hidden prompt or sensitive instruction
- an attempted bypass of AI safety controls
- image-based text containing unsafe content
- steganographically hidden text inside an image

If the content passes all checks, it is forwarded to Gemini for a normal response. Otherwise, the request is blocked.

## Main Application

- `A.py` — main Flask application and security pipeline
- `templates/index.html` — chat interface
- `templates/login.html` — login page mockup/UI
- `Create_Datasets/dbcrete.py` — creates the SQLite dataset database from CSV data
- `Algorithim/ALG Steps.txt` — project workflow and algorithm notes

## Core Workflow

The app follows a multi-layer security process:

1. Receive uploaded image or chat prompt
2. Extract text from images using OCR
3. Store extracted text in SQLite
4. Run Layer 1: exact match detection
5. Run Layer 2: partial keyword/semantic pattern detection
6. Run Layer 3: Gemini-based conceptual malicious intent check
7. Run Layer 4: steganography detection using LSB analysis
8. Allow only clean data to proceed to Gemini

## Folder Structure

```text
v12/
├── A.py
├── .env
├── data.db
├── V12_datasets.db
├── V12_datasets.csv
├── Algorithim/
│   └── ALG Steps.txt
├── Create_Datasets/
│   ├── dbcrete.py
│   ├── V12_datasets.csv
│   └── Test/
│       └── hanu.py
├── Model V12/
├── templates/
│   ├── index.html
│   └── login.html
├── Trial & Test/
│   └── test1.py
├── USER_IMG/
└── README.md
```

## Features

- OCR-based image text extraction using OpenCV + Tesseract
- SQLite database creation and FTS pattern matching
- Malicious prompt dataset loading from CSV
- Gemini AI security screening
- Hidden text detection in images through steganography analysis
- Flask API endpoints for chat and file upload

## Technologies Used

- Python
- Flask
- SQLite
- OpenCV
- Tesseract OCR
- Pillow
- NumPy
- Google Generative AI
- Python-dotenv

## Prerequisites

Before running this project, make sure you have:

- Python 3.9+
- Tesseract OCR installed on your machine
- A valid Google Gemini API key

### Tesseract installation

On Windows:

```powershell
winget install --id=TesseractOCR.Tesseract -e
```

On Ubuntu/Debian:

```bash
sudo apt-get install tesseract-ocr
```

On macOS:

```bash
brew install tesseract
```

## Environment Setup

Create a virtual environment and install the required dependencies:

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
pip install flask pillow pytesseract opencv-python python-dotenv google-generativeai numpy
```

Create a `.env` file in the project root and set your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

You can also use:

```env
GOOGLE_API_KEY=your_api_key_here
```

## Running the Application

From the project root, start the server:

```bash
python A.py
```

Then open:

```text
http://localhost:5000
```

## Important Routes

### `GET /`
Returns the chat web interface.

### `POST /chat`
Accepts JSON in this form:

```json
{
  "prompt": "Hello, can you help me?"
}
```

### `POST /upload`
Accepts an uploaded image file in a multipart form under the field name `image`.

The server will:

- OCR the image
- scan the extracted text
- run malicious-content checks
- either block it or submit it to Gemini

## Database Notes

- `data.db` stores extracted image text records
- `V12_datasets.db` stores malicious pattern data
- `V12_datasets.csv` is the source used to populate the malicious-pattern database

## Safety Considerations

This project is a security-oriented filtering tool. The logic is designed to detect suspicious content before passing input to an LLM. However, for production use, you should:

- keep API keys in a secure environment
- validate all uploaded files
- restrict file types and size limits
- use a proper deployment configuration instead of debug mode

## Possible Improvements

- add user authentication
- add a proper admin dashboard
- support more image formats and stronger OCR tuning
- integrate a real prompt-injection dataset
- add logging and threat reporting
- move configuration to a dedicated settings file

## License

This project does not include a license file. If you plan to distribute or reuse it publicly, add an appropriate license before publishing.
