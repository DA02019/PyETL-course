import requests

url = "https://www.ptt.cc/bbs/Gossiping/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

ss = requests.session()
ss.cookies["over18"] = "1"

res = ss.get(url, headers=headers)

print(res.text)