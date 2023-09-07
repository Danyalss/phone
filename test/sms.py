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


attack_speed = float(input(("" + cyan + "[" + Red + "Enter The " + Blue + "refresh rate of attacks" + cyan + "]─[" + Red + "in seconds :" + cyan + "]" + Reset)))

sleep_time = float(input(("" + cyan + "[" + Red + "Enter the " + Blue + "time between attacks" + cyan + "]─[" + Red + "seconds :" + cyan + "]" + Reset)))

numbert = int(input("" + cyan + "[" + Red + "Enter" + cyan + "]─[" + Blue + "the number" + cyan + "]─[" + Green + "of repetitions :" + cyan + "]" + Red + ": " + Reset))

i = 0




