from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"

file = open("test/sample.py")

code = file.read()

prompt = f""" 

You are a code review assistant.

Analyze the Python code below and identify bugs.

Return ONLY a JSON array.

Each finding must have:
- line: integer
- severity: "low", "medium", or "high"
- message: string

Example:
[
  {{
    "line": 12,
    "severity": "high",
    "message": "..."
  }}
]

Do not report code that is correct.

Python code:
    {code}
"""

# data
# │
# ├── contents
# │     └── What we are sending to the model
# │
# └── generationConfig
#       └── How we want the model to generate the response

data = {
    "contents" : [
        {
            "parts" :[
                {
                    "text" : prompt
                }
            ]
        }
    ],
    "generationConfig" : {
        "temperature" : 0,
        "responseMimeType": "application/json"

    }
}


response = requests.post(url, json = data)
result = response.json() # Take the HTTP response body that is JSON and convert it into Python data."file.close()


# reply content from gemini model
str_text = result["candidates"][0]["content"]["parts"][0]["text"]

def clean_json_text(str_text : str): 
    text = str_text.strip()
    if text.startswith("```"):
        text = text.split("\n",1)[1]
    if text.endswith("```"):
        text = text.rsplit("```",1)[0]
    return text.strip()

def parse_model_json(str_text):
    cleaned = clean_json_text(str_text)
    return json.loads(cleaned)

text = parse_model_json(str_text)
# answer = text["answer"]

print("Answer : ", text)
print("="*50)

# token calculation
prompt_tokens = result["usageMetadata"]["promptTokenCount"]
candidates_tokens = result["usageMetadata"]["candidatesTokenCount"]
total_tokens = result["usageMetadata"]["totalTokenCount"]

print("Prompt tokens (i/p tokens) : ",prompt_tokens)
print("candidates tokens (o/p tokens) : ",candidates_tokens)
print("total_tokens : ",total_tokens )
print("="*50)
# cost caluculation
input_cost = round( (prompt_tokens / 1000000) * 0.25 , 4)
output_cost = round( (candidates_tokens/ 1000000) * 1.50 , 4) 
total_cost = round(input_cost + output_cost , 4)

print(f"input_token_cost : ${input_cost}")
print(f"output_token_cost : ${output_cost}")
print(f"total_token_cost : ${total_cost}")
print("="*50)