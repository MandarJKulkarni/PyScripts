import sys
import requests
import requests_ntlm

urlToConnect = "http://myUrlWhichNeedsWindowsAuthentication/50231/Test"
payload = '''
{
"name":"mjk",
"comments":"temporary",
"AccessLevel":"basic"
}'''
try:
    getResponse =  requests.get(urlToConnect,auth=requests_ntlm.HttpNtlmAuth('winuser','winpassword'))
    postResponse = requests.post(urlToConnect,data=payload,auth=requests_ntlm.HttpNtlmAuth('winusername','winpassword'))
    if postResponse.status_code == 200:
        print ("post request succeeded")
except:
    print("Unexpected error:", sys.exc_info()[1])
