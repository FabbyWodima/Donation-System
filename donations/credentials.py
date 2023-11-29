import requests
import json
import base64
from datetime import datetime
from requests.auth import HTTPBasicAuth

# Mpesa credentials


class MpesaC2bCredential:
    consumer_key = 'oBAPbosveq0E6yo65Rcodehg40luRHox'
    consumer_secret = 'lpE8haFclmA8OHGh'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

class MpesaAccessToken:
    r = requests.get(MpesaC2bCredential.api_URL,
                     auth=HTTPBasicAuth(MpesaC2bCredential.consumer_key, MpesaC2bCredential.consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']


# Lipa na Mpesa mpesa password
class LipanaMpesaPassword:
    lipa_time = datetime.now().strftime('%Y%m%d%H%M%S')
    Business_short_code = "174379"
    OffSetValue = "0"
    passkey = "bfb279f9aa9bdbcf158e97dd71a467cd2e0c893059b10f78e6b72ada1ed2c919"
    data_to_encode = Business_short_code + passkey + lipa_time
    online_password = base64.b64encode(data_to_encode.encode())
    decode_password = online_password.decode('utf-8')

    


access_token = MpesaAccessToken.validated_mpesa_access_token
online_password = LipanaMpesaPassword.decode_password

# STK push request
# url = MpesaC2bCredential.api_URL
# headers = {
#     'Authorization': f'Bearer {access_token}',
#     'Content-Type': 'application/json',
# }

# payload = {
#     'BusinessShortCode': LipanaMpesaPassword.Business_short_code,
#     'Password': online_password,
#     'Timestamp': datetime.now().strftime('%Y%m%d%H%M%S'),
#     'TransactionType': 'CustomerPayBillOnline',
#     'Amount': '1',  
#     'PartyA': '600978',  
#     'PartyB': LipanaMpesaPassword.Business_short_code,
#     'PhoneNumber': '254759391153',  
#     'CallBackURL': 'https://example.com/callback',  
#     'AccountReference': '123456',  
#     'TransactionDesc': 'Payment for XYZ',
# }


# response = requests.request("POST", 'https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest', 
#                             headers = headers, json = payload)
