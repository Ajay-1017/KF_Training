from dotenv import load_dotenv
import os
import requests
import json

class RetryableError(Exception):
    pass

load_dotenv()

API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"


def review_code(code):
    prompt = f""" 

    You are a code review assistant.

    Analyze the Python code below and identify bugs.

    A finding should be reported only when the supplied code actually demonstrates the problem; 
    don't report hypothetical issues that depend on invalid, unsupported, or unusual inputs.

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

    try:
        response = requests.post(url, json = data , timeout=30)
    
        if response.status_code in (429, 500, 503):
                raise RetryableError(
                    f"Gemini temporary failure: HTTP {response.status_code}"
                )

        result = response.json() # Take the HTTP response body that is JSON and convert it into Python data."
        # reply content from gemini model
        str_text = result["candidates"][0]["content"]["parts"][0]["text"]

    except requests.exceptions.Timeout:
        raise Exception("Gemini request timed out")
    
    except requests.exceptions.JSONDecodeError:
        raise Exception("Gemini returned an invalid json response")

    


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
    return text
