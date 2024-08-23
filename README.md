# OCR-NLP-Automator

**OCR-NLP-Automator** is an intelligent document processing system that automates the extraction and analysis of text from scanned documents using Optical Character Recognition (OCR) and Natural Language Processing (NLP) techniques.

This project enables users to upload scanned documents (PDFs, images), convert them into machine-readable text using OCR, and then apply NLP models to classify documents, extract key information (such as names, dates, monetary values), and generate structured outputs for further use.

### Features:
- **OCR Integration**: Converts scanned PDFs or images into editable and searchable text using Tesseract OCR.
- **NLP Pipeline**: Leverages NLP to classify documents, extract key entities (like dates, names, and amounts), and summarize content.
- **Multi-format Support**: Handles various document formats including PDFs, JPEG, PNG, and more.
- **Export to JSON/CSV**: Outputs structured data in JSON or CSV formats for easy integration into other systems.
- **Modular Design**: Easy to extend with custom NLP models or additional document types.

### Tech Stack:
- **OCR**: Tesseract OCR
- **NLP**: Python (SpaCy, NLTK, Hugging Face Transformers)
- **Backend**: Flask/FastAPI (or any backend framework you choose)
- **Frontend (optional)**: React or HTML/CSS for a simple web interface
