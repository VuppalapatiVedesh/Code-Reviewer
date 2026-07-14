import os
from flask import Flask, render_template, request
from dotenv import load_dotenv
from openai import OpenAI
import markdown

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Initialize the OpenAI client configured for Groq
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = None

if GROQ_API_KEY:
    client = OpenAI(
        api_key=GROQ_API_KEY,
        base_url="https://api.groq.com/openai/v1"
    )

@app.route("/", methods=["GET", "POST"])
def index():
    # Keep track of submitted inputs to repopulate the form
    code_input = ""
    selected_language = "python"
    review_output = None
    error_message = None

    # Check if API key is configured
    if not GROQ_API_KEY:
        error_message = "Groq API key is missing. Please create a '.env' file in the project root and add 'GROQ_API_KEY=your_key_here'."

    if request.method == "POST":
        code_input = request.form.get("code", "")
        selected_language = request.form.get("language", "python")

        if not code_input.strip():
            error_message = "Please enter some code to review."
        elif not GROQ_API_KEY or not client:
            error_message = "Cannot review code: Groq API key is not configured. Please add it to your '.env' file."
        else:
            try:
                # System prompt as specified in requirements
                system_prompt = (
                    "You are an expert senior software engineer.\n\n"
                    "Analyze the code carefully.\n\n"
                    "Return ONLY in this format.\n\n"
                    "## Bug Report\n\n"
                    "List all bugs.\n\n"
                    "## Code Explanation\n\n"
                    "Explain the code in beginner friendly language.\n\n"
                    "## Optimized Code\n\n"
                    "Return corrected optimized code inside markdown code blocks."
                )

                # Send request to Groq API
                response = client.chat.completions.create(
                    model="llama-3.3-70b-versatile",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": f"Language: {selected_language}\nCode:\n{code_input}"}
                    ],
                    temperature=0.2, # Keep output relatively deterministic
                )

                raw_markdown = response.choices[0].message.content

                # Convert markdown response to HTML using extensions for formatting
                review_output = markdown.markdown(
                    raw_markdown,
                    extensions=["fenced_code", "codehilite", "tables"]
                )
            except Exception as e:
                error_message = f"An error occurred while communicating with the AI model: {str(e)}"

    return render_template(
        "index.html",
        code=code_input,
        language=selected_language,
        review_output=review_output,
        error_message=error_message
    )

if __name__ == "__main__":
    # Run the Flask app on localhost:5000 in debug mode
    app.run(host="127.0.0.1", port=5000, debug=True)
