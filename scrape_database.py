from urllib.request import Request, urlopen
import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://www.footballdb.com/statistics/nfl/player-stats/passing/2021/regular-season?sort=passrate&limit=all"
hdr = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36",
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
}
req = Request(url, headers=hdr)
page = urlopen(req).read()
# data = requests.get(url).text

soup = BeautifulSoup(page, "html.parser")

# print(soup)
print("Classes of each table:")
for table in soup.find_all("table"):
    print(table.get("class"))
