from bs4 import BeautifulSoup
from requests import get

usr_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}

def _req(company):
    resp = get(
        url="https://www.emploitic.com/offres-d-emploi?q="+company+"&limit=50",
        headers=usr_agent,
    )
    resp.raise_for_status()
    return resp

def search(term):   
    resp = _req(term)
    soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('div', attrs={'id': 'search-result-empty'}) : 
        print("Makach")
        return NULL
    else:
        result_block = soup.find_all('div', attrs={'class': 'row-fluid job-details pointer'})
        for result in result_block:
            link = result.find('a',href=True,title=True)
            if link:
                print (link.get("title"))
                print (link.get("href"))

                adr =  result.find('span', attrs={'class': 'spaced-right'})
                soc = result.find('h6', attrs={'class': 'ellipsis'}).span
                date = result.find('span', attrs={'class': 'spaced-right pull-left'})
                exp = result.find('span', attrs={'class': 'spaced-right phone-display-blok'})
                print (soc.contents[0])
                print (adr.contents[1])
                print (date.contents[1][1:])
                print (str(exp.contents[1])[1:-1])
                print (exp.span.contents[0])
                print("-------------")

    print(len(result_block))



search("Djezzy")
