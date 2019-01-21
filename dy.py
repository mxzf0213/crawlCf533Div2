import requests
from bs4 import BeautifulSoup
import csv

def getContestInfo():
    ContestInfo = []
    url = "https://codeforces.com/contest/1105/standings/page/"
    headers = \
    {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:64.0) Gecko/20100101 Firefox/64.0',
        'Host': 'codeforces.com'
    }

    page_cnt = 0

    while(True):
        page_cnt = page_cnt + 1

        if page_cnt == 28:
            break

        r = requests.get(url+str(page_cnt), headers=headers, timeout=10)
        if r.status_code != 200:
            break

        soup = BeautifulSoup(r.text,'lxml')
        contents = soup.find_all('table',class_='standings')[0].contents[5:]
        l = len(contents)

        for i in range(0,l,4):
            each = contents[i]
            now = []
            now.append(each.td.text.strip())
            now.append(each.a.text.strip())

            for i in range(5,8,2):
                try:
                   now.append(each.contents[i].span.text.strip())
                except:
                    now.append("")
            for i in range(11,28,4):
                try:
                   now.append(each.contents[i].span.text.strip())
                except:
                    now.append("")
            ContestInfo.append(now)
    return ContestInfo

if __name__ == "__main__":
    f = open("contestInfo.csv", "w", newline="")
    csv_writer = csv.writer(f)

    ContestInfo = getContestInfo()
    csv_writer.writerow(['#','Who','=','*','A','B','C','D','E'])
    for each in ContestInfo:
        csv_writer.writerow(each)

    f.close()