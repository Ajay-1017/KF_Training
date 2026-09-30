# a = "  "

# if a.strip():
#     print("true")
# else:
#     print("false")



def mask_phone(password : str) -> str :
    return password[:2] + "******" + password[-2:]

print(mask_phone("7338721670"))