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

def emploiesearch(term):   
    resp = _req(term)
    soup = BeautifulSoup(resp.text, 'html.parser')
    jobs = []
    if soup.find('div', attrs={'id': 'search-result-empty'}) :
        return {"jobs": jobs}
    else:
        result_block = soup.find_all('div', attrs={'class': 'row-fluid job-details pointer'})
        
        for result in result_block:
            link = result.find('a',href=True,title=True)
            if link:
                adr =  result.find('span', attrs={'class': 'spaced-right'})
                soc = result.find('h6', attrs={'class': 'ellipsis'}).span
                date = result.find('span', attrs={'class': 'spaced-right pull-left'})
                exp = result.find('span', attrs={'class': 'spaced-right phone-display-blok'})
                job = {
                    'title': link.get("title"),
                    'link': link.get("href"),
                    'company': soc.contents[0],
                    'adress': adr.contents[1],
                    'date': date.contents[1][1:],
                    'profile': str(exp.contents[1])[1:-1],
                    'experience': exp.span.contents[0]
                }
                jobs.append(job)
        return {"jobs": jobs}
