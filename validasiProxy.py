import requests

with open("freeProxy.txt", "r") as f:
    proxies = f.read().split("\n")

situs = "https://home.amikom.ac.id/"

proxy_succeed = False  
for proxy in proxies:
    try:
        res = requests.get(situs, proxies={"http": proxy, "https": proxy}, timeout=5)
        if res.status_code == 200:
            print(f" Proxy {proxy} accessed successfully {situs}")

            # Buka file untuk menulis (mode 'w' berarti menulis)
            with open('validProxy.txt', 'w') as file:
                # Isi data ke dalam file dengan menggunakan newline ('\n')
                file.write(f'{proxy}\n')

                # Pastikan untuk selalu menutup file setelah selesai
                file.close()
            proxy_succeed = True
            break
    except:
        continue

    if not proxy_succeed:
        print(f" All proxies fail to access {situs}")