import requests

data = "salam"

url = f"https://api.telegram.org/bot6583320212:AAGci8mHu1_ctX1OIQd2rlvqHM-11FIGsZ4/sendmessage?chat_id=1663788795&text={data}"
mypay = {
	"UrlBox": "https://api.komodaa.com/api/v2.6/loginRC/request",
	"ContentTypeBox": "application/json",
	"ContentDataBox": "{\"phone_number\":\"09373058966\",\"force_send_otp\":true}",
	"HeadersBox": "",
	"RefererBox": "",
	"AgentList": "Google+Chrome",
	"AgentBox": "",
	"VersionsList": "HTTP/1.1",
	"MethodList": "POST"
}

send = requests.post(url="https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",data=mypay)


print(send)