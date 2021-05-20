
import urllib.request

# 获取GET请求
# response = urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode("utf-8"))


# 获取POST请求
import urllib.parse

data = bytes(urllib.parse.urlencode({"hello": "word"}), encoding="utf-8")
response = urllib.request.urlopen("http://httpbin.org/post", data=data)
print(response.read().decode("utf-8"))

