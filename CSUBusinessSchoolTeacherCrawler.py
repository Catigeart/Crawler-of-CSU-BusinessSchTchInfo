import requests
from bs4 import BeautifulSoup
f = open('out.txt','w',encoding='utf-8')
idDictionary = {'glkx':'管理科学与信息管理系',
                'qygl':'企业管理系',
                'jrxx':'金融学系',
                'cwtz':'财务投资与管理系',
                'jjmy':'经济与贸易系',
                'kjxx':'会计学系',
                'scyx':'市场营销系',
                'sy':'实验、设备与信息服务中心',
                'xz':'行政',
                }

def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Error"

if __name__ == "__main__":
    url = 'http://bsoa.csu.edu.cn/blog/list'
    soup = BeautifulSoup(getHtmlText(url), 'html.parser')
    div_content = soup.find('div', attrs={'class':'tab-content'})
    for div in div_content.find_all('div', attrs={'class':'tab-pane'}):
        id = div.attrs['id']
        print(idDictionary[id],file=f)
        for link in div.find_all('a'):
            strURL = link.get('href')[57:-3]
            soupTc = BeautifulSoup(getHtmlText('http://bsoa.csu.edu.cn/blog/content2?name='+strURL), 'html.parser')
            divTcBox = soupTc.find('div', attrs={'class': 'perbox'})
            print(divTcBox.text,file=f)
            divTcCon = soupTc.find('div', attrs={'class': 'percon'})
            print(divTcCon.text,file=f)

f.close()