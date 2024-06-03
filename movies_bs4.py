'''this short project introduces beautifulsoup module and shows
how to use it to obtain information about a given url
'''

from bs4 import BeautifulSoup
from bs4.dammit import html_meta
import requests

url = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


html = requests.get(url).content

soup = BeautifulSoup(html, "html.parser")
count = 1
listmovies = soup.find("tbody", {"class":"lister-list"}).find_all("tr", limit=50)
for tr in listmovies:
    title = tr.find("td", {"class":"titleColumn"}).find("a").text
    year = tr.find("td", {"class":"titleColumn"}).find("span").text
    rating = tr.find("td", {"class":"ratingColumn"}).find("strong").text
    print(str(count) + ". " + title.ljust(50) + " "+ year + " = " + rating )
    count += 1
