import json

import httpx


login_payload = {
    "email": "example_1@example.com",
    "password": "098765"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login",
                            json=login_payload)

login_response_data = login_response.json()
print(login_response.status_code)
print(login_response_data)


access_payload = login_response_data["token"]["accessToken"]

headers = {"Authorization": f"Bearer {access_payload}"}

get_response = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers)

get_response_data = get_response.json()

print(get_response.status_code)
print(get_response_data)