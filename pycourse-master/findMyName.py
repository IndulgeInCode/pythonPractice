from urllib import request,parse
import urllib
import http.cookiejar
from bs4 import BeautifulSoup

#word=input("请输入搜索的名字:");
#url="http://www.baidu.com/s?wd="+urllib.parse.quote(word);
url="http://www.baidu.com/s?wd="+urllib.parse.quote("冯宣祯");
headers={"Accept": "text/html, application/xhtml+xml, image/jxr, */*",

         "Accept - Encoding": "gzip, deflate, br",

         "Accept - Language": "zh - CN",
         
         "Cookie": "BIDUPSID=A74087E71F7DAB292772116C8CA9A41A; PSTM=1572958227; BD_UPN=12314753; BAIDUID=922A4F29D4941620CD7C193D89A306FC:FG=1; BDUSS=VXbGdpbjBWVFRLYjEtYXpLZ0hXNENMR0YwMEp6Vnk5dkpXQjNCdVFGaW9Lfk5kRVFBQUFBJCQAAAAAAAAAAAEAAAAJPX-g6dnX07HIuMrV4cvhAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAKiey12onstdNk; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; delPer=0; BD_CK_SAM=1; PSINO=2; H_PS_PSSID=1437_21089_20697_29567_29699_29221_26350; COOKIE_SESSION=3607_0_8_6_6_6_0_0_7_5_152_0_0_0_116_0_1574302096_0_1574305587%7C9%230_0_1574305587%7C1; BDRCVFR[dG2JNJb_ajR]=mk3SLVN4HKm; userFrom=www.baidu.com; BDRCVFR[-pGxjrCMryR]=mk3SLVN4HKm; H_PS_645EC=b12dOuIdxW8YdGq%2B9O487CSivoDkjLaElmYV4B6YVnWVEbJ8fO3hm%2FR%2B%2FzU",

         "Connection": "Keep - Alive",
         "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 Edge/16.16299",
         "referer":"baidu.com"};
cjar = http.cookiejar.CookieJar();
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar));

headall=[];
for key,value in headers.items():
    item=(key,value);
    headall.append(item);
opener.addheaders=headall;
urllib.request.install_opener(opener);
data =urllib.request.urlopen(url).read().decode('utf-8');
soup=BeautifulSoup(data,'html.parser');
# 以格式化的形式打印html
#print(soup.prettify());
for result_table in soup.find_all('h3',class_='t'):

    a_click = result_table.find("a");

    print( "-----标题----\n" + a_click.get_text())  # 标题
    print("----链接----\n" + str(a_click.get("href")))  # 链接