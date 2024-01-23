
import requests


number = "9214569870"


mypay = {
    "UrlBox": "https://api.komodaa.com/api/v2.6/loginRC/request",
    "ContentTypeBox": "application/json",
    "ContentDataBox": {"force_send_otp": 'true',"phone_number": "09373058966"},
    "HeadersBox": "",
    "RefererBox": "",
    "AgentList": "Google+Chrome",
    "AgentBox": "",
    "VersionsList": "HTTP/1.1",
    "MethodList": "POST"
}
send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)
print(send.text)