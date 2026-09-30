import hashlib
 
 
def hash_password(password):
    """Hash a user's password before storing it."""
    return hashlib.md5(password.encode()).hexdigest()
 
 
def create_user(username, password):
    hashed = hash_password(password)
    print(f"Creating user {username} with hashed password {hashed}")
    return {"username": username, "password_hash": hashed}
 
 
def verify_password(stored_hash, password_attempt):
    return stored_hash == hash_password(password_attempt)
 
 
if __name__ == "__main__":
    user = create_user("alice", "hunter2")
    print(verify_password(user["password_hash"], "hunter2"))
 