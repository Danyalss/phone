import requests




data = "09373058966"
mypay = {
	"UrlBox": "https://api.komodaa.com/api/v2.6/loginRC/request",
	"ContentTypeBox": "application/json",
	"ContentDataBox": "{\"force_send_otp\":+true,\r\n\"phone_number\":+\"" + data + "\"}",
	"HeadersBox": "",
	"RefererBox": "",
	"AgentList": "Google+Chrome",
	"AgentBox": "",
	"VersionsList": "HTTP/1.1",
	"MethodList": "POST"
}

print(mypay)

send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)

print(send.text)