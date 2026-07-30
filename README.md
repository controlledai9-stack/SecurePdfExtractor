# 📄 PDF Text Extractor

A simple and efficient PDF Text Extractor built with Python and Streamlit. This application allows users to upload PDF documents and instantly extract all readable text, making it useful for working with reports, research papers, books, notes, and other digital documents.

This project is designed as a beginner-friendly introduction to PDF processing and file handling using Python.

---

## ✨ Features

* 📄 Upload PDF documents
* 📝 Extract text from every page
* ⚡ Fast and lightweight processing
* 🎨 Interactive Streamlit interface
* 📚 Supports multi-page PDF files
* 📋 Display extracted text in the browser
* 💻 Easy to run locally

---

## 🛠️ Tech Stack

* Python
* Streamlit
* PyPDF2

---

## 📂 Project Structure

```text
pdf-text-extractor/
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd <YOUR_PROJECT_FOLDER>
```

### 2. Create a virtual environment

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Mac/Linux**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

---

## 🚀 How It Works

1. Launch the application.
2. Upload a PDF file.
3. The application reads each page using PyPDF2.
4. All readable text is extracted and combined.
5. The extracted text is displayed in the Streamlit interface.

---

## 📦 Required Packages

* streamlit
* PyPDF2

Install them using:

```bash
pip install -r requirements.txt
```

---

## ⚠️ Limitations

This project is intended for learning and basic PDF processing.

Current limitations include:

* ❌ Cannot extract text from scanned or image-based PDFs
* ❌ Does not perform Optical Character Recognition (OCR)
* ❌ Does not preserve complex formatting or layouts
* ❌ Does not extract images or tables

For scanned documents, OCR libraries such as Tesseract can be integrated in future versions.

---

## 🌱 Future Improvements

Possible enhancements include:

* 🔍 OCR support for scanned PDFs
* 📑 Extract tables and images
* 💾 Download extracted text as a TXT file
* 📄 Export extracted text to PDF or DOCX
* 📚 Batch processing of multiple PDFs
* 🔎 Search within extracted text
* 🤖 AI-powered document summarization

---

## 📸 Screenshots

You can add screenshots of:

* Home Screen
* PDF Upload Interface
* Extracted Text Output

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push your branch.
5. Open a Pull Request.

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Developed as a beginner-friendly Python project to learn PDF processing, file handling, and interactive web application development using Streamlit.
