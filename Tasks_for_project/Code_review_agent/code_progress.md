# 1) call the model

```Python
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"


data = {
    "contents" : [
        {
            "parts" :[
                {
                    "text" : "replay with ok"
                }
            ]
        }
    ]
}

response = requests.post(url, json = data)
result = response.json() # json() method that converts json body into python objects

text = result["candidates"][0]["content"]["parts"][0]["text"]
prompt_tokens = result["usageMetadata"]["promptTokenCount"]
candidates_tokens = result["usageMetadata"]["candidatesTokenCount"]



print("Answer : ", text)
print("Prompt tokens (i/p tokens) : ",prompt_tokens)
print("candidates tokens (o/p tokens) : ",candidates_tokens)
```

# 2) Find the token count

```Python
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"

file = open("sample.py")
code = file.read()

data = {
    "contents" : [
        {
            "parts" :[
                {
                    "text" : f"Analyze this Python code: {code}"
                }
            ]
        }
    ]
}

response = requests.post(url, json = data)
result = response.json() # json() method that converts json body into python objects
file.close()

# reply content from gemini model
text = result["candidates"][0]["content"]["parts"][0]["text"]
# print("Answer : ", text)


# token calculation
prompt_tokens = result["usageMetadata"]["promptTokenCount"]
candidates_tokens = result["usageMetadata"]["candidatesTokenCount"]
total_tokens = result["usageMetadata"]["totalTokenCount"]

print("Prompt tokens (i/p tokens) : ",prompt_tokens)
print("candidates tokens (o/p tokens) : ",candidates_tokens)
print("total_tokens : ",total_tokens )


# cost caluculation
input_cost = round( (prompt_tokens / 1000000) * 0.25 , 4)
output_cost = round( (candidates_tokens/ 1000000) * 1.50 , 4) 
total_cost = input_cost + output_cost

print(f"input_token_cost : ${input_cost}")
print(f"output_token_cost : ${output_cost}")
print(f"total_token_cost : ${total_cost}")
```

# 3) Change the temparture

```python
from dotenv import load_dotenv
import requests
import os

load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"

file = open("sample.py")
code = file.read()

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
                    "text" : f"Analyze this code : {code} and summarize your analysis in 2-3 sentences."
                }
            ]
        }
    ],
    "generationConfig" : {
        "temperature" : 1
    }
}


response = requests.post(url, json = data)
result = response.json() # json() method that converts json body into python objects
file.close()

# reply content from gemini model
text = result["candidates"][0]["content"]["parts"][0]["text"]
print("Answer : ", text)

# token calculation
prompt_tokens = result["usageMetadata"]["promptTokenCount"]
candidates_tokens = result["usageMetadata"]["candidatesTokenCount"]
total_tokens = result["usageMetadata"]["totalTokenCount"]

print("Prompt tokens (i/p tokens) : ",prompt_tokens)
print("candidates tokens (o/p tokens) : ",candidates_tokens)
print("total_tokens : ",total_tokens )

# cost caluculation
input_cost = round( (prompt_tokens / 1000000) * 0.25 , 4)
output_cost = round( (candidates_tokens/ 1000000) * 1.50 , 4) 
total_cost = round(input_cost + output_cost , 4)

print(f"input_token_cost : ${input_cost}")
print(f"output_token_cost : ${output_cost}")
print(f"total_token_cost : ${total_cost}")
```

```
output :

Temperature 0: The model produced the same or highly consistent answer for the same prompt.
Temperature 1: The model produced more variation in both the wording and output token count 
for the same prompt.
```

# 4) Get JSON instead of a paragraph

```Python
from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"

file = open("sample.py")

code = file.read()

prompt = f""" 
Analyze this code : {code} and return JSON with exactly one field named answer, 
whose value is a string  and summarize your analysis in 2-3 sentences.
Do not wrap the JSON in ```json or ``` code fences.
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
result = response.json() # Take the HTTP response body that is JSON and convert it into Python data."
file.close()


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
answer = text["answer"]

print("Answer : ", answer)
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
```

# 5) Write the first review prompt

```python
from dotenv import load_dotenv
import os
import requests
import json


load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"

file = open("auth.py")

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
print("="*50
```

# 7) Write the scorer

### **main.py**

```python
from dotenv import load_dotenv
import os
import requests
import json



load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-lite:generateContent?key={API_key}"


def review_code(code):
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
    result = response.json() # Take the HTTP response body that is JSON and convert it into Python data."

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
    return text



if __name__ == "__main__":
    with open("test/7_test_password_check.py") as file :
    
        code = file.read() 
        text = review_code(code)
        print(text)
```

### **scorer.py** 

```python
# True  = bug expected
# False = no bug expected
import os
from main import review_code
test_files = {
    "1_test_sql_injection.py" : True,
    "2_test_hardcoded_secret.py" : True,
    "3_test_md5_password_hashing.py" : True,
    "4_test_missingKey.py" : True,
    "5_test_unclosed_file.py" : True,
    "6_test_safe_divison.py" : False,
    "7_test_password_check.py" : False,
}

passed = 0 

for filename , expected_bug in test_files.items():
    file = open(os.path.join("test/",filename))
    code = file.read()
    findings = review_code(code)
    if(
        expected_bug and findings  or
        not expected_bug and not findings
    ):
        passed+=1
        print(f"{filename} -> PASS")
    else:
        print(f"{filename} -> FAIL")

print(f"Score: {passed}/{len(test_files)}")
```
