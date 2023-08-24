url_trip = "https://gateway.trip.ir/api/Totp"
json_trip = {"PhoneNumber": "0" + number}


req_trip = requests.post(url=url_trip,json=json_trip,headers=random_head)
print("trip",req_trip)







url_rghm = "https://api.rghm.ir/users/code"
json_rghm = {
	"phone": "+98" + number
}


req_rghm = requests.post(url=url_rghm,json=json_rghm)
print("rghm",req_rghm)