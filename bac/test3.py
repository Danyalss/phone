import requests
import random
import json

number = "9373058966"
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






url_ = "https://www.tebinja.com/api/v1/users"
json_ = {
	"captchaHash": "",
	"captchaValue": "",
	"username": "09373058966"
}


req = requests.post(url=url_, json=json_, headers=random_head)

# چاپ status code پاسخ
print(req.status_code)

# چاپ محتوای پاسخ به صورت خام
print(req.content)

# چاپ محتوای پاسخ به صورت JSON (اگر پاسخ در فرمت JSON باشد)
try:
    response_json = req.json()
    print(json.dumps(response_json, indent=4, ensure_ascii=False))
except json.JSONDecodeError:
    print("پاسخ قابل تبدیل به JSON نیست.")