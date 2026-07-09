import requests
import os
# https://xkcd.com/353/ -> import antigravity (python funny comic website) 

# https://imgs.xkcd.com/comics/python.png -> Direct URL of the comic image

image = requests.get("https://imgs.xkcd.com/comics/python.png")

base_dir = os.path.dirname(__file__)

with open(os.path.join(base_dir,'comic_image.png'),'wb') as file:
    file.write(image.content) # it returns byte content of the image from the website


website = requests.get("https://xkcd.com/353/")

# print(r)  # -> Prints the HTTP response object (e.g., <Response [200]>)

# print(dir(r))  # Shows all available attributes and methods of the Response object

# help(r) # -> Displays documentation for the Response object

# print(website.text) # -> print html representation of website

print(website.status_code)
print(website.headers)

print(type(website.content))

# Server
#    │
#    │ Sends bytes
#    ▼
# 01001000 01010100 01001101 01001100 ...
#    ▼
# requests
#    ▼
# website.content   (bytes)

print(website.content)

