import json
import pprint
import os

import requests

folder_path = "./photo"
if not os.path.exists(folder_path):
    os.mkdir(folder_path)

url = "https://www.nownews.com/nn-client/api/v1/cat/column/?pid=6085665"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

# json_data = json.loads(res.text)
# pprint.pprint(json_data)

# 確定request回傳的東西是json形式
# pprint.pprint(res.json())

json_data = res.json()

for article_obj in json_data["data"]["newsList"]:
    post_title = article_obj["postTitle"]
    post_url = "www.nownews.com" + article_obj["postUrl"]
    image_url = article_obj["imageUrl"]
    image_content = requests.get(image_url, headers=headers).content
    image_type = image_url.split('.')[-1].split('?')[0]
    image_path = f"{folder_path}/{post_title}.{image_type}"

    with open(image_path, "wb") as f:
        f.write(image_content)

    print(post_title)
    print(post_url)
    print(image_url)
    print(image_path)
    print("=======")

