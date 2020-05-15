import http.client
import json

def get_auth_token(client = None):
    conn = http.client.HTTPSConnection("rmgmex.auth0.com")
    client_test = str(client).lower()
    print(client_test)
    if client_test is None:
        client_id = "sxYQ7M2f6eS4uEMdu3K5lODdNGz4sBXc"
        client_secret = "xGFrcFtuONTBDxRuiI1Anvaaj-96poESnt_1_L22H8emQZRT-7uS3x1y7Bp7FGhc"
        
    elif client_test == 'executive producer':
        client_id = "sxYQ7M2f6eS4uEMdu3K5lODdNGz4sBXc"
        client_secret = "xGFrcFtuONTBDxRuiI1Anvaaj-96poESnt_1_L22H8emQZRT-7uS3x1y7Bp7FGhc"
        
    elif client_test == 'casting director':
        client_id = "O4B39zpI79jA4Lw9nqs48d4QOPchdJuL"
        client_secret = "Xy1RCUK-9lZRyX33fBtrHoh-u7LvEbNB5_q9Ygs44leqcwW7mN_zrox6T7YHxC8H"
    
    elif client_test == 'casting assistant':
        client_id = "ahoPjYAxwZv3U300wuBVE6Tg4DGYHWis"
        client_secret = "6fhtK_omkYoEsgsrTwVoApDh0-qV5XY2HkVKzVY3Cgn18acvi-cNKau_Y-gBbEga"
    
    else:
        return {
            "success": False,
            "message": "RBAC role not existant"
        }
        
    payload = "{\"client_id\":\"%s\",\"client_secret\":\"%s\",\"audience\":\"capstone\",\"grant_type\":\"client_credentials\"}" % (client_id, client_secret)

    headers = { 'content-type': "application/json" }

    conn.request("POST", "/oauth/token", payload, headers)

    res = conn.getresponse()
    data = res.read()

    return json.loads(data.decode("utf-8"))