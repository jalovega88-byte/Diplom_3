
import requests
import uuid

from urls import BASE_URL


def create_test_user():
    unique_id = uuid.uuid4().hex[:10]

    user_data = {
        "email": f"test_{unique_id}@example.com",
        "password": "TestPassword123",
        "name": "Test User"
    }

    response = requests.post(
        f"{BASE_URL.rstrip('/')}/api/auth/register",
        json=user_data,
        timeout=15
    )

    response.raise_for_status()

    return user_data, response.json()

    
def delete_test_user(access_token):
    response = requests.delete(
        f"{BASE_URL.rstrip('/')}/api/auth/user",
        headers={
            "Authorization": access_token
        },
        timeout=15
    )

    response.raise_for_status()
    return response.json()

