from bs4 import BeautifulSoup
from requests import get
import re


usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}
url = "https://paulgo.io/search"


def page(url,company):
    resp = get(
        url,
        params={
            "q":company,
            "language":"fr"
            },
        headers=usr_agent
    )
    resp.raise_for_status()
    return resp


def search(query):
    dork = "inurl:linkedin.com/company "
    url = url
    resp = page(url,dork+query)
    soup = BeautifulSoup(resp.text, 'html.parser')
    if (query==""): 
        return {"companies": []}
    if soup.find('div', attrs={'class': 'dialog-error'}) :
        return {"companies": []}
    else:
        result_block = soup.find_all('article', attrs={'class': 'result'})
        for index, result in enumerate(result_block, start=1):
            if "linkedin.com/company" in result.h3.a["href"]:
                companyname = result.h3.text.split(" | ")[0]
                link = result.h3.a["href"]
                desc = result.p.text
                print("---------------------------------")
                print(index)
                print(companyname)
                print(link)
                print(desc)

                results = {
                    "rank":index,
                    "name":companyname,
                    "link":link,
                    "desc":desc
                }
        return {"results" :results}

search("atm mobilis")