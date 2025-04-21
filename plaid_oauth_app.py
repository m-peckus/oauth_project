#!/usr/bin/env python3

import os
import requests
from dotenv import load_dotenv

# Load keys from .env file
load_dotenv()
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")


def create_link_token():
    url = "https://sandbox.plaid.com/link/token/create"
    payload = {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "client_name": "My Finance App",
        "user": {
            "client_user_id": "user-123"
        },
        "products": ["auth", "transactions"],
        "country_codes": ["US"],
        "language": "en",
        #"redirect_uri": "http://localhost:5000/callback"
    }

    response = requests.post(url, json=payload)
    return response.json()

print(create_link_token())
