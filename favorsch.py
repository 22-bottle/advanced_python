import requests
from bs4 import BeautifulSoup
from datetime import datetime

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
url = "https://datalab.naver.com/keyword/realtimeList.naver?age=20s"
response = requests.get(url,headers=headers)

# print(response.text) # html 코드

# print(response.text)
# print(response.url)
# print(response.content)
# print(response.encoding)
# print(response.headers)
# print(response.json)
# print(response.links)
# print(response.ok)
# print(response.status_code)

soup = BeautifulSoup(response.text, 'html.parser')

#print(soup.title)
#print(soup.title.string)
#print(soup.span)
#print(soup.findAll("span"))

#file = open("daum.html","w")
#file.write(response.text)
#file.close()

rank = 1
results = soup.findAll("span","item_title")

search_rank_file = open("rankresult.txt","a")

print(datetime.today().strftime("%y년 %m월 %d일의 실시간 검색어 순위입니다.\n"))
for result in results:
    search_rank_file.write(str(rank)+"위: "+result.get_text()+"\n")
    print(rank,"위 : ",result.get_text(),"\n")
    rank += 1