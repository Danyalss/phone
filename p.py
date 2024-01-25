

import requests




def send(url_for_send, json_for_send, random_head):
    try:
        send_att = requests.post(url=url_for_send, json=json_for_send,timeout=2.5)
    except Exception as e:
        if str(e) == "('Connection aborted.', RemoteDisconnected('Remote end closed connection without response'))" or "Read timed out" in str(e):
            pass
        else:
            #bot.send_message(admin_id, f"خطایی رخ داد: {e}")
            with open('backup/error.txt', 'a') as f:
                f.write(f"{e}\n")


number = '9373058966'

url_divar = "https://api.divar.ir/v5/auth/authenticate"
json_divar = {"phone":number}

random_head = "jngdagn"

send(url_divar,json_divar,random_head)  
