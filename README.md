# Plaid OAuth Flow Demo (Sandbox)

![App Demo](Plaid-OAuth_2.gif)

This project is a compact Flask web application that demonstrates the OAuth-style token exchange workflow using the [Plaid API](https://plaid.com/).   
It recreates how third-party applications can securely access user financial data without handling or storing user credentials directly.

## Features

- Generates a `link_token` via backend request to Plaid
- Displays a basic HTML interface to connect a test bank account using Plaid Link
- Receives a `public_token` upon successful authentication
- Exchanges the `public_token` for a long-lived `access_token`
- Fully sandbox-based for safe development and learning

## Technologies Used

- Python 3
- Flask
- HTML/JavaScript
- Plaid API (Sandbox Environment)
- dotenv

## Project Structure

.   
├── app.py # Flask app with both endpoints   
├── .env   # Plaid API credentials (not shared)  
├── requirements.txt # Project dependencies     
├── templates/   
│   └── index.html # Simple HTML frontend  
│── static/   
│   └── favicon.png # Favicon file

## Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/m-peckus/oauth_project.git
   cd oauth_project

2. Create a .env file with your credentials

PLAID_CLIENT_ID=your_client_id  
PLAID_SECRET=your_sandbox_secret

4. Install dependencies  
pip install flask python-dotenv requests

4. Run the application  
python app.py

5. To access the app open your browser at  
   http://localhost:5000  

Project is deployed live at the following URL: https://plaid-sandbox-oauth.onrender.com  

OAuth Flow Summary

1. Backend creates a link_token

2. Frontend uses the token to initiate a secure connection with a test bank

3. Upon success, Plaid returns a public_token

4. The app exchanges this for an access_token, used to access user-specific financial data


Educational Purpose  
This project is intended for learning purposes only.   
It uses Plaid’s Sandbox environment and does not connect to real financial institutions.





