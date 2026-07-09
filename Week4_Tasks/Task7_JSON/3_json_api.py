import requests
import json
url = "https://open.er-api.com/v6/latest/USD"

response = requests.get(url)

data = response.json()

print(type(data))
print(len(data['rates'])) # How many rates
print(round(20*(data['rates']['INR']),2)) # USD -> INR

# dump the python object into a json file

with open("KF_training/Week4_Tasks/Task7_JSON/json_api.json",'w') as f:
    json.dump(data,f,indent=2)


# practice (without using json from reponse)

# import requests
# import json
# url = "https://open.er-api.com/v6/latest/USD"

# response = requests.get(url)

# python_str = response.text
# print(type(python_str))

# python_dict = json.loads(python_str)
# print(type(python_dict))

# json_str = json.dumps(python_dict,indent=2)
# print(type(json_str))


