import json
import re
from urllib.parse import urlparse

f = open('results.json')
results = json.load(f)

def googlesearch():
    companies = []
    urls = results
    urls = results.get("urls")
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
                tld = tld.split(".")
                if len(tld) > 2: tld[0] = "www"
                tld = '.'.join(tld)
                u = u._replace(query="",netloc=tld).geturl()

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
            finalcomp = []
            companies.append(company)
            while(len(companies)>0):
                finalcomp.append(companies[0])
                for fcomp in finalcomp:
                    for company in companies:
                        if company.get("url") == finalcomp[0].get("url"):
                            if (fcomp.get("company") == "") and (company.get("company") != ""): fcomp["company"] = company.get("company")
                            if (fcomp.get("size") == "") and (company.get("size") != ""): fcomp["size"] = company.get("size")
                            if (fcomp.get("headquarters") == "") and (company.get("headquarters") != ""): fcomp["headquarters"] = company.get("headquarters")
                            if (fcomp.get("industries") == "") and (company.get("industries") != ""): fcomp["industries"] = company.get("industries")
                            if (fcomp.get("specialties") == "") and (company.get("specialties") != ""): fcomp[specialties] = company.get("specialties")
                            if (fcomp.get("type") == "") and (company.get("type") != ""): fcomp["type"] = company.get("type")
                            if (fcomp.get("about") == "") and (company.get("about") != ""): fcomp["about"] = company.get("about")
                            if (fcomp.get("website") == "") and (company.get("website") != ""): fcomp["website"] = company.get("website")

    return {"companies": companies}
    
res = googlesearch()
print (res)