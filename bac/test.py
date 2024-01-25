import requests
import re





number = "9214569870"

url_ = "https://gw.taaghche.com/v4/site/auth/login"
json_ = {
	"contact": "0"+number,
	"forceOtp": 'false'
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

s = "<strong>Status: 200 / OK</strong>"

# Extract the status code using a regular expression
status_code_str = re.search(r'Status: (\d+)', s).group(1)

# Convert the extracted status code to an integer
status_code = int(status_code_str)

# Print the status code
print(f"<strong>Status: {status_code} / OK</strong>")