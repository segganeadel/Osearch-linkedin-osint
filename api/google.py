import json
import re
from urllib.parse import urlparse
import gsearch



f = open('results.json')
results = json.load(f)

def search (keyword):
    query = 'inurl:linkedin.com "company size" '+ keyword
    client = gsearch.SearchClient(
        query,
        tbs="li:1",
        max_search_result_urls_to_return=100,
        http_429_cool_off_time_in_minutes=45,
        http_429_cool_off_factor=1.5,
        # proxy="socks5h://127.0.0.1:9050",
        verbosity=1,
        verbose_output=True,  # False (only URLs) or True (rank, title, description, and URL)
    )
    client.assign_random_user_agent()
    urls = client.search()
    return {"urls": urls}


def googlesearch(keyword):
    
    urls = search(keyword)
    urls = results.get("urls")
    companies = []
    for url in urls:
        if url: 
            companyname = url.get("title").split(" | ")[0]
            if companyname:
                desc = url.get("description")
                s = re.search(r"Company size: (.+?)\. ?",desc)
                if s : size = s.group(1)
                else : size = ""

                h = re.search(r"Headquarters: (.+?)\. ?",desc)
                if h : headquarters = h.group(1)
                else : headquarters = ""

                i = re.search(r"Industries: (.+?)\. ?",desc)
                if i : industries = i.group(1)
                else : industries = ""

                sp = re.search(r"Specialties: (.+?)\. ?",desc)
                if sp : specialties = sp.group(1)
                else : specialties = ""

                t = re.search(r"Type: (.+?)\. ?",desc)
                if t : type = t.group(1)
                else : type = ""

                a = re.search(r"About us. (.+?)\. ?",desc)
                if a : about = a.group(1)
                else : about = ""

                w = re.search(r"Website: (.+?)(\. )",desc)
                if w : website = w.group(1)
                else : website = ""

                u = url.get("url")
                u = urlparse(u)
                tld = u.netloc
                #tld = tld.split(".")
                #if len(tld) > 2: tld[0] = "www"
                #tld = '.'.join(tld)
                u = u._replace(query="",netloc=tld,scheme="https").geturl()

                company = {
                    "company": companyname,
                    "size": size,
                    "headquarters": headquarters,
                    "industries": industries,
                    "specialties": specialties,
                    "type": type,
                    "about": about,
                    "website": website,  
                    "url": u,
                    "rank": url.get("rank")
                }
            companies.append(company)
    print(len(companies))
    finalcomp = []
    while(len(companies)>0):
        fcomp = companies.pop(0)
        for company in reversed(companies):
            if company.get("company") == fcomp.get("company"):
                #if (fcomp.get("company") == "") and (company.get("company") != ""): fcomp["company"] = company.get("company")
                if (fcomp.get("size") == "") and (company.get("size") != ""): fcomp["size"] = company.get("size")
                if (fcomp.get("headquarters") == "") and (company.get("headquarters") != ""): fcomp["headquarters"] = company.get("headquarters")
                if (fcomp.get("industries") == "") and (company.get("industries") != ""): fcomp["industries"] = company.get("industries")
                if (fcomp.get("specialties") == "") and (company.get("specialties") != ""): fcomp[specialties] = company.get("specialties")
                if (fcomp.get("type") == "") and (company.get("type") != ""): fcomp["type"] = company.get("type")
                if (fcomp.get("about") == "") and (company.get("about") != ""): fcomp["about"] = company.get("about")
                if (fcomp.get("website") == "") and (company.get("website") != ""): fcomp["website"] = company.get("website")
                companies.remove(company)
        finalcomp.append(fcomp)
    print(len(companies))
    print(len(finalcomp))
    return {"companies": finalcomp}
    
res = googlesearch()
print (res)
