#-------------find access token from a url---------------
from urllib.parse import urlparse, parse_qs

def extract_access_token_from_url(url):
    # Parse the URL
    parsed_url = urlparse(url)

    # Get the fragment part of the URL
    fragment = parsed_url.fragment

    # Parse the fragment into key-value pairs
    fragment_params = parse_qs(fragment)

    # Get the access token
    access_token = fragment_params.get("access_token", [None])[0]
    print(access_token)

    return access_token

full_url = "http://localhost:8000/callback#state=sso_request&access_token=ya29.a0AfB_byAzhMSsblxHR1Uw6KM86Ts1-QaHudiR63vSo1nOqLs-EKbajuaTYbveMjWO1UFABxRtBlXo66ISObfetk1-uY4ny6Z5awxmb76QzspL8X3sKFcLcwQpkIHx5_QlHF-2YbLW93GX7iJePorIJdKObVBt7zN14SIVUgaCgYKAUkSARASFQHsvYlsmV5SXWYz-5-bZshxTLaETQ0173&token_type=Bearer&expires_in=3599&scope=email%20profile%20https://www.googleapis.com/auth/userinfo.profile%20https://www.googleapis.com/auth/userinfo.email%20openid&authuser=0&prompt=consent"

access_token = extract_access_token_from_url(full_url)

if access_token:
    print("Access Token:", access_token)
else:
    print("Access Token not found in the URL.")