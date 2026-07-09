import requests

# 1)get

# pay_load={"page":2,"count":25}

# r = requests.get("https://httpbun.com/get",params=pay_load)

# r = requests.get("https://httpbun.com/get?page=3&count=100") # (same as above)

# print(r.text)
# print(r.url)


# =======================================================================================================

# 2)post

# pay_load = {"user_name":"ajay","password":"testing"}

# r = requests.post("https://httpbun.com/post",data = pay_load )

# r_dict = r.json() # creates a python dictionary from a python response 

# print(r.text)
# print(r_dict['form'])


# =======================================================================================================

# 3) basic authetication

# r = requests.get("https://httpbun.com/basic-auth/ajay/testing",auth=("ajay","testing"))
# print(r)
# print(r.text)



# =======================================================================================================

# 4)  delay and timeout

r = requests.get("https://httpbun.com/delay/6",timeout=3)
print(r)

# =======================================================================================================