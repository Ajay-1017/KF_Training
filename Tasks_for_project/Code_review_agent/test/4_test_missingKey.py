def get_user_email(user):
    name = user["name"]
    email = user["email"]
    print(f"{name}: {email}")
    return email
 
user = {"name": "Ajay"}
get_user_email(user)
 