import requests
import credentials

message = ''
description = ''
body = ''

requests.post('https://api.mynotifier.app', {
    "apiKey": credentials.api_key,  # This is your own private key
    "message": message,
    "description": description,
    "body": body, 
    "type": "info",  # info, error, warning or success,
    },
    timeout=None
)
