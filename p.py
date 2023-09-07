import requests

def test_proxy(proxy_ip, proxy_port):
    proxies = {
        'http': f'http://{proxy_ip}:{proxy_port}',
        'https': f'https://{proxy_ip}:{proxy_port}',
    }
    try:
        response = requests.get('http://digikala.com', proxies=proxies)
        print(response)
        if response.status_code == 200:
            return True
        else:
            return False
    except:
        return False

# تست یک پروکسی
proxy_ip = '104.28.214.161'
proxy_port = 8080
if test_proxy(proxy_ip, proxy_port):
    print(f' {proxy_ip}:{proxy_port}            True')
else:
    print(f' {proxy_ip}:{proxy_port}            false')
