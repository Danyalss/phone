
import requests


number = "9214569870"

url_ = "https://api.irangard.com/api/Users/Register/Token"
json_ = {
	"username": "0"+number
}

mypay = {
    "UrlBox": {url_},
    "ContentTypeBox": "application/json",
    "ContentDataBox": json_,
    "HeadersBox": "",
    "RefererBox": "",
    "AgentList": "Google+Chrome",
    "AgentBox": "",
    "VersionsList": "HTTP/1.1",
    "MethodList": "POST"
}
send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)
print(send.text)