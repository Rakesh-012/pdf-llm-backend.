# PDF-LLM Backend

A FastAPI-based backend service for uploading PDF documents, extracting their content, and using a Large Language Model (LLM) Gemini to generate summaries and answer questions based on the PDF content.

## Features

- Upload PDF and extract text using `pdfplumber`
- Store and retrieve documents from MongoDB
- Generate summaries using LLMs (Gemini)
- Answer contextual questions about the document using LLMs
- JWT-based authentication for LLM operations
- Pagination for document listing
- Dockerized for containerized deployment

## Directory Structure

```

pdf_llm_backend/
│
├── app/
│   ├── models/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── requirements.txt
├── Dockerfile
├── .env
├── README.md

```

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/pdf-llm-backend.git
cd pdf-llm-backend
````

### 2. Create `.env` File

Create a `.env` file using `.env` as a template and set the following variables:

```bash
JWT_SECRET=your_jwt_secret
MONGO_URI=mongodb://localhost:27017
GEMINI_API_KEY=your_google_gemini_api_key
```

* Replace `your_google_gemini_api_key` with your actual Gemini API key.

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000/docs`.

## Docker (Optional)

To build and run the app using Docker:

```bash
docker build -t pdf-llm-backend .
docker run -p 8000:8000 --env-file .env pdf-llm-backend
```

## Testing

You can test the API through the built-in Swagger UI at:

```
http://127.0.0.1:8000/docs
```

## Assumptions

* Assumed mock PDF files are uploaded via the `/documents/upload` endpoint.
* No frontend is required for this project.
* Gemini is used as default LLM.
