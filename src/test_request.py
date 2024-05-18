import requests
import argparse

class DummyInfo(object):
    """docstring for DummyInfo"""
    def __init__(self):
        super(DummyInfo, self).__init__()
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzkxMTgzMjMsInN1YiI6MTQsImp3dF92ZXJzaW9uIjoidmVyc2lvbl8wLjAuMSIsInN1YnNjcmlwdGlvbl9zdGF0dXMiOiJndWVzdCJ9.8JVrB5s3Tu_l0fxH1T-GITZfhmhxGwiyQRsfiJCcBw4"
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzkxNjc1NjcsInN1YiI6MSwiand0X2lkIjoxLCJqd3RfdmVyc2lvbiI6InZlcnNpb25fMC4wLjEiLCJzdWJzY3JpcHRpb25fc3RhdHVzIjoiZ3Vlc3QifQ.W5zErSE8Mp5EQiKzYrbXNLQ2gWNiXvgnSMgpX-szKIU"
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2NzkzNTI3ODcsInN1YiI6Miwiand0X2lkIjoyLCJqd3RfdmVyc2lvbiI6InZlcnNpb25fMC4wLjEiLCJzdWJzY3JpcHRpb25fc3RhdHVzIjoiZ3Vlc3QifQ.CkxfcoYm1EBt9hYaQumJF1wpH6G-m3nc1xSZrIyPqWo"
        # token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEyNTk3MzAsInN1YiI6Mywiand0X2lkIjozLCJqd3RfdmVyc2lvbiI6InZlcnNpb25fMC4wLjEiLCJzdWJzY3JpcHRpb25fc3RhdHVzIjoiZ3Vlc3QifQ.4ITQb6OPb4ab_FgNJboibiUDQf_S5wrY6Q1oU1qMJS0"

        self.token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE3MTEyODE0MzUsInN1YiI6NCwiand0X2lkIjo0LCJqd3RfdmVyc2lvbiI6InZlcnNpb25fMC4wLjEiLCJzdWJzY3JpcHRpb25fc3RhdHVzIjoiZ3Vlc3QifQ.G4gc89N_WJ2sApnCjlsR_yWvprzah10VHjOYWRDV1Ik"
        self.google_token = "eyJhbGciOiJSUzI1NiIsImtpZCI6ImFjZGEzNjBmYjM2Y2QxNWZmODNhZjgzZTE3M2Y0N2ZmYzM2ZDExMWMiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJhenAiOiI4Njg3ODQ2NTYzNTMtZGo4aHBjazA3b2FrbG1tbWoyYWE2ZWZhcWpicjNwOXQuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJhdWQiOiI4Njg3ODQ2NTYzNTMtZGo4aHBjazA3b2FrbG1tbWoyYWE2ZWZhcWpicjNwOXQuYXBwcy5nb29nbGV1c2VyY29udGVudC5jb20iLCJzdWIiOiIxMTIyNDIyNzIyMTQwMTA4NTQ4NTgiLCJlbWFpbCI6Im5ham11ejFzYWtpYkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXRfaGFzaCI6IlM4emFnN0p3NG8zbVprRUM3LUs1UGciLCJub25jZSI6Ik14VTM0VFlhaHA3Qm1Ta2JfMy1hMXAzYmVjbUk4WGNRTVUyOUdkZFNYWlUiLCJuYW1lIjoibmFqbXV6IHNha2liIiwicGljdHVyZSI6Imh0dHBzOi8vbGgzLmdvb2dsZXVzZXJjb250ZW50LmNvbS9hL0FHTm15eGFQMG01d1N2R3FVZWo4MkR4bGpkUmNGcExzZzdpdTZRYkRUTjlyPXM5Ni1jIiwiZ2l2ZW5fbmFtZSI6Im5ham11eiIsImZhbWlseV9uYW1lIjoic2FraWIiLCJsb2NhbGUiOiJlbiIsImlhdCI6MTY4MDg0NjM3MiwiZXhwIjoxNjgwODQ5OTcyfQ.WtwZjrW1klGW6bnDXt99GwMP2UkAZOBTQLAQgdxrK4D-Ds7_zGZiyVL-0861JRc9Z31B0PMMVNos5inE-uN5LWO15KcdCeMIfbla4oD8fadAMbTn8dZWgCN2TCsXGOzyz-1JLUVZ-6zyKM8NuVY1WVtOX1Q_RmZsVBXm_GHZc_MVcy6Pt2-KjlRJb-kaq1RxgK__bHLaphmeM60SsFxG7zf_Pqe1yvaUILerphecJhlAh4wHMSz16CfS3rrb6b0se1JLX23MvK3CSUadzna38-sfJo1988xnN3GzODLvmAr7s8H3vzhk4vl7JF08gwj9enyXSXrA_dlKn9pw1IIe2g"


info = DummyInfo()

parser = argparse.ArgumentParser()
parser.add_argument("--route", help="Endpoint route. Example: \'guest/token\'")
parser.add_argument("--token", help="Auth token", default=f"{info.token}")
# base_url = "http://192.168.0.102:8090"
base_url = "http://127.0.0.1:8900"
# url = "http://127.0.0.1:8900/guest/update/push_token?push_token=abcsdfd"



def test_guest_token(url):
    print("called")
    user_id = "dummy_1_user_id"
    push_token = "dummy_1_push_token"
    
    device_id = 'dummy_1_device_id'
    device_os = 'dummy_1_device_os'
    device_model = 'dummy_1_device_model'
    platform = 'dummy_1_platform'
    app_id = 'dummy_1_app_id'
    app_version = 'dummy_1_app_version'

    
    headers = {
        'accept': 'application/json',
        # 'Content-Type': 'application/json',
    }
    
    json_data = {
        'user_id': user_id,
        'push_token': push_token,

        'device_id': device_id,
        'device_os': device_os,
        'device_model': device_model,
        'platform': platform,
        'app_id': app_id,
        'app_version': app_version,
    }
    response = requests.post(url, headers=headers, json=json_data)

    if response.ok:
        print(response.json())
    else:
        print(response.status_code, response.reason)

def test_guest_verify(url, token):
    headers = {"authorization": f"Bearer {token}"}
    response = requests.get(url, headers=headers)

    if response.ok:
        print(response.json())
    else:
        print(response.status_code, response.reason)

def test_google_login(url, token):
    google_token = info.google_token
    headers = {
        "Authorization": f"Bearer {token}", 
        "Authorization-Google": f"Bearer {google_token}"
    }
    response = requests.post(url, headers=headers)

    if response.ok:
        print(response.json())
    else:
        print(response.status_code, response.reason)

def test_apple_token(url, token):
    auth_code = "c5f87914fc29d4b948813cc5f85083240.0.srxtu.kF6Plv66RdYxs3wZSIuFWg"
    url = url + f"?authorization_code={auth_code}"

    headers = {"Authorization": f"Bearer {token}"}
    response = requests.post(url, headers=headers)

    if response.ok:
        print(response.json())
    else:
        print(response.status_code, response.reason)

def test_apple_login(url, token):
    apple_token = "eyJraWQiOiJmaDZCczhDIiwiYWxnIjoiUlMyNTYifQ.eyJpc3MiOiJodHRwczovL2FwcGxlaWQuYXBwbGUuY29tIiwiYXVkIjoiY29tLnRvdWNoNGZlZWwuc3NvLWV4YW1wbGUiLCJleHAiOjE2ODI1MjczOTEsImlhdCI6MTY4MjQ0MDk5MSwic3ViIjoiMDAxNzM0LjkyMTFjYzdjZWVlOTQ5ZTliMGY5MDlhYzEwNWU2NGZkLjE1MzUiLCJhdF9oYXNoIjoiVU80aVFHYnVPTVNzaGJUdTJmLTJCUSIsImVtYWlsIjoiZzlzZ3Btd3p6eUBwcml2YXRlcmVsYXkuYXBwbGVpZC5jb20iLCJlbWFpbF92ZXJpZmllZCI6InRydWUiLCJpc19wcml2YXRlX2VtYWlsIjoidHJ1ZSIsImF1dGhfdGltZSI6MTY4MjQ0MDk1Mywibm9uY2Vfc3VwcG9ydGVkIjp0cnVlfQ.uAoQZYyhDMANhCD0wgK3FGYs56TwsBrtAM3Y-HBuVyP3_gr0RbeCNypFIIgiVEVtRcuaEMoTmNd29p7sddze1u2EsERM3Byn9gu3-V11uFGWucuW1CkBnBJREFSEvdReLN3kJeeVlLmO_jAbNKAwEij1loCmelRqs4LMfwhP2g8RlBAlFYs5XAAZyUBAEUimK6d4TRgm36uJTZ7rJMzPketp-qIB6M2nEwTc2zlQxvbwxmBjQiMXnL8E_k69OMN-6Hoo_LMiGw4HcAPq8IoabWkEtNLWKlKxmnCgshm3I7e1QBp_ESomTEPc0EQIlFmtcOnTFxhRKQVgqY-dNqVHkQ"

    headers = {"Authorization": f"Bearer {token}", "authorization_token": f"Bearer {apple_token}"}

    response = requests.post(url, headers=headers)

    # print(response.json())
    if response.ok:
        print(response.json())
    else:
        print(response.status_code, response.reason)


if __name__ == "__main__":
    args = parser.parse_args()

    new_token = info.token
    if not args.token is None:
        new_token = args.token

    if args.route == "guest/token":
        test_guest_token(url=f"{base_url}/guest/token")
    elif args.route == "guest/verify":
        test_guest_verify(url=f"{base_url}/guest/verify", token=new_token)
    elif args.route == "google/login":
        test_google_login(url=f"{base_url}/google/login", token=new_token)
    elif args.route == "apple/token":
        test_apple_token(url=f"{base_url}/apple/token", token=new_token)
    elif args.route == "apple/login":
        test_apple_login(url=f"{base_url}/apple/login", token=new_token)

