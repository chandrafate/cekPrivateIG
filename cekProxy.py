import threading
import queue
import requests

q = queue.Queue()
valid_proxies = []

with open("freeProxy.txt", "r") as f:
    proxies = f.read().split("\n")
    for p in proxies:
        q.put(p)

def check_proxies():
    global q
    global valid_proxies

    while not q.empty():
        proxy = q.get()
        try:
            # res = requests.get("https://auth.amikom.ac.id/", proxies={"http":proxy, "https:": proxy})
            res = requests.get("http://ipinfo.io/json", proxies={"http":proxy, "https:": proxy})
        except:
            continue
        if res.status_code == 200:
            # print(proxy)
            # valid_proxies.append(proxy)
            data = res.json()
            print(f"ip : {data['ip']} {data['country']}")

threads = []

for _ in range(10):
    thread = threading.Thread(target=check_proxies)
    threads.append(thread)
    thread.start()

# Menunggu semua thread selesai
for thread in threads:
    thread.join()

# with open('validProxy.txt', 'w') as file:
#     for proxy in valid_proxies:
#         file.write(f"{proxy}\n")
#     file.close()