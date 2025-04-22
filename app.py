#!/usr/bin/env python3

import os
import requests
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv

# Load API keys from .env
PLAID_CLIENT_ID = os.getenv("PLAID_CLIENT_ID")
PLAID_SECRET = os.getenv("PLAID_SECRET")

app = Flask(__name__)

@app.route("/")
def index():
    # Generate link token
    url = "https://sandbox.plaid.com/link/token/create"
    payload = {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "client_name": "My Finance App",
        "user": {"client_user_id": "user-123"},
        "products": ["auth", "transactions"],
        "country_codes": ["US"],
        "language": "en"
    }
    response = requests.post(url, json=payload)
    link_token = response.json().get("link_token")
    return render_template("index.html", link_token=link_token)

@app.route("/get_access_token", methods=["POST"])
def get_access_token():
    public_token = request.json.get("public_token")
    url = "https://sandbox.plaid.com/item/public_token/exchange"
    payload = {
        "client_id": PLAID_CLIENT_ID,
        "secret": PLAID_SECRET,
        "public_token": public_token
    }
    response = requests.post(url, json=payload)
    return jsonify(response.json())

if __name__ == "__main__":
    app.run(debug=True)
