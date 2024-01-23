import requests

number = "9373058966"

url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

send = requests.post(url=url_divar,json=json_divar)

print(send)