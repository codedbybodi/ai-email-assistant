from google import genai
from google.genai import types

client = genai.Client(api_key="AIzaSyBw8NhO-LRbhCeM4h3PcidnfNM3b4jZGxI")

def generate_replies(email_text):
    prompt = f"""You are a Professional email assistant
Read the following email and write exactly 3 different professional reply options.
Label them clearly as Option 1, Option 2, and Option 3.
Each option should have a different tone: formal, friendly, and concise.

Email:
{email_text}"""
    
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=prompt
    )
    return response.text

print("=== AI Email Reply Assistant ==\n")
print("Paste your email below. when done, type 'END' on a new line:\n")

lines = []
while True:
    line = input()
    if line.strip().upper() == "END":
        break
    lines.append(line)

email_text = "\n".join(lines)
print("\n=== Generating 3 Reply Options.. ===\n")
print(generate_replies(email_text))

