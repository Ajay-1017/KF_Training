import bcrypt

def check_password(password, stored_hash):
    if bcrypt.checkpw(password.encode(), stored_hash):
        return True
    return False

stored_hash = bcrypt.hashpw(b"correct_password", bcrypt.gensalt())
print(check_password("correct_password", stored_hash))