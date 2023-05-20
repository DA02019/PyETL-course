from urllib import request

url = "http://httpbin.org/get"

# 存放在記憶體裡
res = request.urlopen(url=url)
# print(res)
# print(res.read())
# print(res.read().decode("utf-8"))  # 記憶體的東西只能讀取一次
# print(type(res.read().decode("utf-8")))

# 宣告變數接住記憶體裡的東西才可以重複使用
html = res.read()
print(html)
print(html.decode("utf-8"))
