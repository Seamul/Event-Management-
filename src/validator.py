from oauthlib.oauth2 import WebApplicationClient
import requests

GOOGLE_CLIENT_ID = "YOUR_CLIENT_ID"
GOOGLE_CLIENT_SECRET = "YOUR_CLIENT_SECRET"
GOOGLE_TOKEN_INFO_URL = "https://www.googleapis.com/oauth2/v3/tokeninfo"

def validate_google_token(access_token):
    client = WebApplicationClient(GOOGLE_CLIENT_ID)

    # Send a request to Google's token info endpoint to verify the token
    response = requests.get(
        GOOGLE_TOKEN_INFO_URL,
        params={"access_token": access_token}
    )

    if response.status_code == 200:
        token_info = response.json()
        # Check if the audience matches your client ID
        if token_info.get("aud") == GOOGLE_CLIENT_ID:
            return True
    return False
