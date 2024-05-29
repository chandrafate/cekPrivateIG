import requests
import time

def cek_profile(username, bot_token, chat_id):
    url = f"https://i.instagram.com/api/v1/users/web_profile_info/?username={username}"
    headers = {
        "x-ig-app-id": "936619743392459",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9,ru;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept": "*/*",
    }

    try:
        proxies = {
            'http': 'http://iukygyqc-rotate:7k34vj0az56e@p.webshare.io:80/',
            'https': 'http://iukygyqc-rotate:7k34vj0az56e@p.webshare.io:80/',
        }
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        
        data = response.json()
        is_private = data["data"]["user"]["is_private"]
        
        if not is_private:
            url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
            params = {
                "chat_id": chat_id,
                "text": f"{username} instagram change to PUBLIC"
            }
            response = requests.get(url, params=params)
            data = response.json()
            if data['ok']:
                print("Pesan terkirim!")

    except requests.exceptions.RequestException as e:
        print("An error occurred:", e)

while True:
    usernames = ["yollandapf", "chandrafate", "nxpera_"]
    bot_token = '5376123708:AAF0E_GoacXEm67g5EGI-u3UJ6GsduyoKII'
    chat_id = '1285761234'

    for user in usernames:
        cek_profile(user, bot_token, chat_id)

    print("Sleep 30 minutes...")
    time.sleep(30 * 60)

    
