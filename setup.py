import os
from requests import Session
import sys

host = os.environ.get("AMAZEEAI_BASE_URL")
key = os.environ.get("AMAZEEAI_API_KEY")
email = os.environ.get("AMAZEEAI_USER_EMAIL")
name = os.environ.get("AMAZEEAI_USER_NAME")
password = os.environ.get("AMAZEEAI_USER_PASSWORD")

if not host or not key or not email or not password or not name:
    print("Missing setup configuration")
    sys.exit(1)

session = Session()
session.post(
    url="http://127.0.0.1:8800/api/v1/auths/signup",
    json={
        "email": email,
        "name": name,
        "password": password,
    },
)

session.request(
    method="POST",
    url="http://127.0.0.1:8800/openai/config/update",
    json={
        "ENABLE_OPENAI_API": True,
        "OPENAI_API_BASE_URLS": [host],
        "OPENAI_API_KEYS": [key],
        "OPENAI_API_CONFIGS": {"0": {}},
    },
)
