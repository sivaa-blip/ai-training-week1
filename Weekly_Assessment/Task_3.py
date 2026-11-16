import hashlib
import hmac
import os
from dotenv import load_dotenv
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry


def verify_signature(payload: str | bytes, signature: str, secret: str | bytes) -> bool:
    if isinstance(payload, str):
        payload = payload.encode("utf-8")
    if isinstance(secret, str):
        secret = secret.encode("utf-8")

    expected_signature = hmac.new(
        key=secret,
        msg=payload,
        digestmod=hashlib.sha256,
    ).hexdigest()

    return hmac.compare_digest(expected_signature, signature)


def main():
    # 1. Load credentials from .env
    load_dotenv()
    api_key = os.getenv("API_KEY", "default_api_key")
    webhook_secret = os.getenv("WEBHOOK_SECRET", "default_webhook_secret")

    # 2. Configure requests.Session with Retry
    session = requests.Session()
    retries = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retries)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    session.headers.update({"Authorization": f"Bearer {api_key}"})

    # 3. GET JSONPlaceholder users and print first 5 users
    url = "https://jsonplaceholder.typicode.com/users"
    response = session.get(url, timeout=10)
    response.raise_for_status()
    users = response.json()

    for user in users[:5]:
        print(f"{user.get('id')} - {user.get('name')} - {user.get('email')}")

    # 4. Using .get() only, print details of the first user
    first_user = users[0] if users else {}
    address = first_user.get("address", {})
    city = address.get("city", "Not Available")
    zip_code = address.get("zip", "Not Available")

    print(f"City: {city} | Zip: {zip_code}")

    # 5. HMAC-SHA256 signature verification tests
    payload = '{"event": "user.created", "id": 1}'
    valid_signature = hmac.new(
        key=webhook_secret.encode("utf-8"),
        msg=payload.encode("utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()

    tampered_payload = '{"event": "user.created", "id": 999}'
    wrong_secret = "wrong_secret_key"

    valid = verify_signature(payload, valid_signature, webhook_secret)
    tampered = verify_signature(tampered_payload, valid_signature, webhook_secret)
    wrong = verify_signature(payload, valid_signature, wrong_secret)

    print(f"Valid: {valid} | Tampered: {tampered} | Wrong secret: {wrong}")


if __name__ == "__main__":
    main()
