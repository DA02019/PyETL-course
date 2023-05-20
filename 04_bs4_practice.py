import requests
from bs4 import BeautifulSoup

url = "https://www.ptt.cc/bbs/joke/index.html"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

res = requests.get(url, headers=headers)

# print(res.text)
soup = BeautifulSoup(res.text, "html.parser")

# print(soup)


# find
log_tag_object = soup.find("a", {"id": "logo"})
# findAll -> List
# log_tag_object_list = soup.findAll("a", {"id": "logo"})
log_tag_object_list = soup.findAll("a", id="logo")

print(log_tag_object)
print(log_tag_object_list)


# select_one
log_tag_object = soup.select_one('a[id = "logo"]')
# select
log_tag_object_list = soup.select("a#logo")

print(log_tag_object)
print(log_tag_object_list)


print(log_tag_object_list[0])
print(log_tag_object_list[0].text)
print("https://www.ptt.cc" + log_tag_object_list[0]["href"])

print("==================")

title_tag_list = soup.select('div.title')  # returns a list of tag
print("[title_tag_list[0]]", title_tag_list[0])
print("[title_tag_list[0].find('a')]", title_tag_list[0].find('a'))
print("[title_tag_list[0].find('a').text]", title_tag_list[0].find('a').text)
print("[title_tag_list[0].find('a')[\"href\"]]", title_tag_list[0].find('a')["href"])

print("==================")

print(type(soup))
print(type(title_tag_list[0].find('a')))
