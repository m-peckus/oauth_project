#!/usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

# Load keys from .env file
load_dotenv()
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")

# Replace this with the public token you got from the frontend
public_token = "public-sandbox-50ede66a-1e7c-4919-a96f-58bd906b367e"

url = "https://sandbox.plaid.com/item/public_token/exchange"
payload = {
    "client_id": PLAID_CLIENT_ID,
    "secret": PLAID_SECRET,
    "public_token": public_token
}

response = requests.post(url, json=payload)
print(response.json())