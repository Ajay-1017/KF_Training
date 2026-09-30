import requests

test_code = '''

import sqlite3

def get_user(username):
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    query = "SELECT * FROM users WHERE username = '" + username + "'"
    cursor.execute(query)
    return cursor.fetchone()

'''

response = requests.post(
    "http://localhost:8000/reviews",
    json={"source_code": test_code}
)

print(response.content)











