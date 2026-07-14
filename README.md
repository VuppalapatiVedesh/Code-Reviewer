# Intelligent Code Reviewer & Explainer

A modern, responsive web application powered by **Flask** and the **Groq API (Llama 3.3)** that provides instant, professional code reviews, explanations, and optimized code recommendations for Python, JavaScript, and Java files.

This project is built using a clean, minimalist design with a premium glassmorphic dark-theme container. It is structured perfectly to upload directly to GitHub for internships or project submissions.

---

## Features

- **Automated Bug Reports**: Instantly detects syntax errors, logical issues, and bad practices.
- **Beginner-Friendly Explanations**: Breaks down what your code is doing in simple, easy-to-understand terms.
- **Code Optimization**: Suggests corrected and highly optimized code block formats.
- **Support for Key Languages**: Python, JavaScript, and Java support.
- **Responsive & Modern UI**: Centered glassmorphic card interface, gradients, rounded buttons, and input validation.
- **Vanilla Setup**: Lightweight, zero complex JavaScript frameworks.

---

## Folder Structure

```text
CodeReviewer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── templates/
│      index.html
│
└── static/
       style.css
```

---

## Installation & Setup

### Prerequisite
Ensure you have **Python 3.8+** installed.

### 1. Clone the repository
```bash
git clone https://github.com/your-username/CodeReviewer.git
cd CodeReviewer
```

### 2. Create a Virtual Environment
Initialize a fresh Python virtual environment to manage dependencies:
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Requirements
Install all necessary packages via `pip`:
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a file named `.env` in the root directory:
```bash
# Windows (cmd/Powershell) or manual creation
echo GROQ_API_KEY=your_groq_api_key_here > .env
```
Open the `.env` file and replace `your_groq_api_key_here` with your actual Groq API key (e.g. `gsk_...`).

### 5. Run the Application
Launch the Flask development server:
```bash
python app.py
```
Open your browser and navigate to:
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## Code Quality & Technical Stack
- **Backend**: Python 3, Flask, `python-dotenv` for config management.
- **AI Integrations**: Groq API using standard OpenAI Python Client (utilizing model `llama-3.3-70b-versatile`).
- **Markdown rendering**: Python `markdown` library with `codehilite` and `fenced_code` extensions for beautiful presentation.
- **Frontend**: Vanilla HTML5 structure and custom CSS3 Styling (no external frameworks like Tailwind/Bootstrap/React).
