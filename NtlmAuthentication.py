#Demo for using requests package to call REST APIs
#Usage of requests_ntlm package for windows authentication

import requests
import requests_ntlm

urlToConnect = "http://myUrlWhichNeedsWindowsAuthentication/50231/Test"
payload = '''
{
"name":"mjk",
"comments":"temporary",
"AccessLevel":"basic"
}'''

getResponse =  requests.get(urlToConnect,auth=requests_ntlm.HttpNtlmAuth('winuser','winpassword'))
postResponse = requests.post(urlToConnect,data=payload,auth=requests_ntlm.HttpNtlmAuth('winusername','winpassword'))
