import os
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

os.system("pip install requests")
time.sleep(1)
os.system("pip install tqdm")
time.sleep(1)
os.system("pip install emoji")
time.sleep(1)
print("" + cyan + "[" + yellow + "All packages" + cyan + "]─[" + Blue + "are" + cyan + "]─[" + Green + "installed" + cyan + "]" + Red + ": " + Reset)
time.sleep(8)
os.system("clear")
