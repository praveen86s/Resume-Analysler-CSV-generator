# AI-Powered Resume Analyzer & CSV Generator 📄🚀

An automated pipeline built to streamline recruitment processes by extracting structured information from bulk resumes. This tool accepts a ZIP file of PDF resumes, uses **Google Gemini** to analyze the text, and generates a structured CSV for easy candidate management.

## 🌟 Overview
HR teams often struggle with the manual task of opening and reading hundreds of resumes. This project solves that problem by:
1. **Bulk Processing:** Automatically reading multiple resumes from a single ZIP file.
2. **AI Intelligence:** Understanding unstructured layouts using the **Gemini** model.
3. **Structured Extraction:** Ensuring data consistency (Names, Skills, Experience) using **LangChain's TypedDict Output Parser**.
4. **Data Export:** Providing an instant CSV download for filtering and ranking.

## 🛠️ Tech Stack
- **LLM:** Google Gemini
- **Framework:** [LangChain](https://www.langchain.com/)
- **Parsing:** [PyMuPDF (fitz)](https://pymupdf.readthedocs.io/)
- **Interface:** [Streamlit](https://streamlit.io/)
- **Data:** Pandas
- **Environment Management:** Python-Dotenv

## ✨ Key Features
- **Fast PDF Extraction:** High-speed text parsing from PDF documents.
- **Smart Data Mapping:** Extracts Full Name, Email, Phone, Skills, Education, and a Brief Summary.
- **Progress Tracking:** Real-time progress bar during bulk analysis.
- **Security:** Uses environment variables for API key protection.

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+
- A Google Gemini API Key (Get it from [Google AI Studio](https://aistudio.google.com/))

### 2. Installation
Clone the repository and install the dependencies:
```bash
git clone https://github.com/your-username/resume-analyzer.git
cd resume-analyzer
pip install -r requirements.txt
