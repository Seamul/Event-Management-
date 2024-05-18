# ---------------------call validate-token---------------
import requests

def validate_access_token(access_token):
    url = "http://localhost:8900/validate-token"  # Update with the actual URL of your FastAPI app
    headers = {"Content-Type": "application/json"}
    data = {"access_token": access_token}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        if "user_info" in result:
            return result["user_info"]
        else:
            return "Token is valid but user info is not available."
    elif response.status_code == 400:
        return "Token is invalid."
    else:
        return "An error occurred while validating the token."

# Example usage:
# access_token = "ya29.a0AfB_byAzhMSsblxHR1Uw6KM86Ts1-QaHudiR63vSo1nOqLs-EKbajuaTYbveMjWO1UFABxRtBlXo66ISObfetk1-uY4ny6Z5awxmb76QzspL8X3sKFcLcwQpkIHx5_QlHF-2YbLW93GX7iJePorIJdKObVBt7zN14SIVUgaCgYKAUkSARASFQHsvYlsmV5SXWYz-5-bZshxTLaETQ0173 Access Token: ya29.a0AfB_byAzhMSsblxHR1Uw6KM86Ts1-QaHudiR63vSo1nOqLs-EKbajuaTYbveMjWO1UFABxRtBlXo66ISObfetk1-uY4ny6Z5awxmb76QzspL8X3sKFcLcwQpkIHx5_QlHF-2YbLW93GX7iJePorIJdKObVBt7zN14SIVUgaCgYKAUkSARASFQHsvYlsmV5SXWYz-5-bZshxTLaETQ0173"  # Replace with the actual access token
# user_info = validate_access_token(access_token)
# print(user_info)
access_token = "ya29.a0AfB_byAzhMSsblxHR1Uw6KM86Ts1-QaHudiR63vSo1nOqLs-EKbajuaTYbveMjWO1UFABxRtBlXo66ISObfetk1-uY4ny6Z5awxmb76QzspL8X3sKFcLcwQpkIHx5_QlHF-2YbLW93GX7iJePorIJdKObVBt7zN14SIVUgaCgYKAUkSARASFQHsvYlsmV5SXWYz-5-bZshxTLaETQ0173"  # Replace with the actual access token

# Call the validate_access_token function
user_info = validate_access_token(access_token)
print(user_info)