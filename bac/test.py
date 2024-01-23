
import requests
import re





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


text = send.text

match = re.search(r'Status: (\d+)', text)

if match:
    # اگر چنین خطی پیدا شد، عدد بعد از "Status: " چاپ می‌شود
    print(match.group(1))
else:
    print("عبارت مورد نظر در متن پیدا نشد.")


print(send.text)
