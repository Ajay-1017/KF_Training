import sys

import requests


if len(sys.argv) != 2:
    print("Usage: python payment_simulator.py <order_id>")
    raise SystemExit(1)

order_id = int(sys.argv[1])

payload = {
    "order_id": order_id,
    "status": "success",
}

response = requests.post(
    "http://127.0.0.1:8000/webhooks/payment",
    json=payload,
)

print("Status:", response.status_code)
print("Response:", response.json())
