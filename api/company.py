from bs4 import BeautifulSoup
from requests import get
import re
from urllib.parse import urlparse


usr_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'}


def page(company):
    url = "https://paulgo.io/search"

    resp = get(
        url,
        params={
            "q": company,
            "language": "fr"
        },
        headers=usr_agent
    )
    resp.raise_for_status()
    return resp


def Company(id):

    company = {
        "companyname": "",
        "size": "",
        "headquarters": "",
        "address": "",
        "address2": "",
        "industries": "",
        "specialties": "",
        "type": "",
        "about": "",
        "founded": "",
        "website": "",
        "url": ""
    }
    link = "https://fr.linkedin.com/company" + id
    if (link == ""):
        return {"company": company}
    dork = "inurl:"
    u = link
    u = urlparse(u)
    u = u._replace(scheme="").geturl()

    for atribute in company.keys():

        if atribute == "url":
            company["url"] = link

        if atribute == "companyname":
            
            resp = page(link)
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if link in result.h3.a["href"]:
                    company["companyname"] = result.h3.text.split(" | ")[0]

        if atribute == "website":
            resp = page(dork + u +" Site web")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Site web:? (.+?)( |\. )",desc)
                    if s : company["website"] = s.group(1)
        

        if atribute == "headquarters":
            resp = page(dork + u +" Siège social")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Siège social: (.+?)\. ?",desc)
                    if s : company["headquarters"] = s.group(1)


        if atribute == "size":

            resp = page(dork + u +" Taille de entreprise")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Taille de l'entreprise:? (.+?) employés",desc)
                    if s : company["size"] = s.group(1)

        if atribute == "industries":

            resp = page(dork + u+" Secteurs")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Secteurs: (.+?)\. ?",desc)
                    if s : company["industries"] = s.group(1)      

        if atribute == "specialties":

            resp = page(dork + u +" Domaines")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Domaines: (.+?)\. ?",desc)
                    if s : company["specialties"] = s.group(1)   

        if atribute == "type":

            resp = page(dork + u +" Type")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Type: (.+?)\.\n?",desc)
                    if s : company["type"] = s.group(1)

        if atribute == "founded":

            resp = page(dork + u +" Fondée en")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Fondée en: (.+?)\. ? ",desc)
                    if s : company["founded"] = s.group(1)  

        if atribute == "address":

            resp = page(dork + u +" Lieux Principal")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Lieux. Principal. (.+?)\. ?(Obtenir l'itinéraire.|$|\n)",desc)
                    if s : company["address"] = s.group(1)   

        if atribute == "address2":

            resp = page(dork + u +" Lieux Principal")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in result.h3.a["href"]:
                    desc = result.p.text
                    s = re.search(r"Obtenir l'itinéraire. (.+)",desc)
                    if s : company["address2"] = s.group(1)    

        if atribute == "about":

            resp = page(dork + u + " a propos")
            soup = BeautifulSoup(resp.text, 'html.parser')
            result_block = soup.find_all('article', attrs={'class': 'result'})
            for result in result_block:
                if u in reversed(result.h3.a["href"]):
                    desc = result.p.text
                    s = re.search(r".+ \|.+ abonnés sur LinkedIn. (.+)",desc)
                    if s : company["about"] = s.group(1)                         
    return {"company":company}                   
                        


"""   
 soup = BeautifulSoup(resp.text, 'html.parser')
    if soup.find('div', attrs={'class': 'dialog-error'}):
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
                    "rank": index,
                    "name": companyname,
                    "link": link,
                    "desc": desc
                }
        return {"companies": results}

"""
