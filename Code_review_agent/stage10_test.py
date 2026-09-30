from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_KEY}"


prompt = """
    Review the supplied code and identify security vulnerabilities.

    Only make claims about functions, variables, classes, and behavior that are actually present in the supplied code.

    Never assume that a missing function, variable, class, or behavior exists.
    If the requested function or behavior is not present in the supplied code, explicitly state that it cannot be analyzed.

    For this exercise, the function delete_user() may be mentioned in the instructions, but you must not invent or assume its implementation if it is not present in the supplied code.

    Return the result as valid JSON.

    Supplied code:

    def add(a, b):
        return a + b

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

response = requests.post(url,json = data)

result = response.json()
text = result.get("candidates")[0].get("content").get("parts")[0].get("text")
print(text)