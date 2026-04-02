from flask import Flask, request, render_template_string
from google import genai
from google.genai import types

app = Flask(__name__)
client = genai.Client(api_key="YOUR-API-KEY")

HTML = """
<!DOCTYPE html>
<html>
    <head>
        <title>AI Email Reply Assistant</title>
    </head>
    <body style="font-family: Arial; max-width: 700px; margin: 40px auto; padding: 20px;">
        <h2>AI Email Reply assistant</h2>
        <form method="POST">
            <textarea name="email" rows="8" style="width: 100%; font-size: 14px; " placeholder="Paste the email you received here...">
                {{ email }}
            </textarea>
            <br>
            <button type="submit" style="padding: 10px 20px; font-size: 16px;">
                Generate 3 Replies
            </button>
            {% if replies %}
            <hr>
            <h3>Reply Options: </h3>
            <pre style="background: #f4f4f4; padding: 15px; white-space: pre-wrap">
                {{ replies }}
            </pre>
            {% endif %}
    </body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    replies = ""
    email = ""
    if request.method == "POST":
        email = request.form["email"]
        prompt = F"""You are a Professional email assistant
Read the following email and write exactly 3 different professional reply options.
Label them clearly as Option 1, Option 2, and Option 3.
Each option should have a different tone: formal, friendly, and concise.

Email:
{email}"""
        
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents=prompt
        )
        replies = response.text
    return render_template_string(HTML , replies=replies, email=email)

if __name__ == "__main__":
    app.run(debug=True)
