import configuration
import requests
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.header)

response = post_new_user(data.user_body)
print(response.status_code)
print(response.json())

auth_token = response.json()["authToken"]

def post_new_client_kit(kit_new_body, auth_token):
    headers = data.header
    if auth_token:
        headers["Authorization"] = "Bearer " + auth_token
    return requests.post(
        configuration.URL_SERVICE + configuration.KITS_PATH,
        json=kit_new_body,
        headers=headers,
    )


response= post_new_client_kit(data.kit_body,auth_token)
print(response.status_code)
print(response.json())