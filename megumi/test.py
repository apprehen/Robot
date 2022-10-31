import requests
url='https://iw233.cn/api.php?sort=random'
pic = requests.get(url)
print(pic.url)