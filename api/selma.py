# coding=utf-8 
#('selmaosint@gmail.com', '#Osint-2022')

from linkedin_api import Linkedin 

# Authenticate using any Linkedin account credentials

api = Linkedin('selmaosint@gmail.com', '#Osint-2022')

#l'utilisateur chooses a company

company_name=str(input("Enter a company name :\n")).strip()

print("Your target is : "+company_name)

#--------------------------------------------------------------------1---------------------------------------------------------------------------#

#D'abord on fait une recherche sur les pages existants sur LInkedIn pour cette entreprise

companies=api.search_companies(keywords=str(company_name))

#"companies" est une liste de dictionnaires
cpt=1

for company in companies : #parcourir la liste
    print("**************company number :"+str(cpt)+"******************")
    print("Company Name : "+str(company["name"]))
    #par exemple, si on veux afficher urn_id, name, headline, et subline :
    print("Urn id : "+str(company["urn_id"])+"\nCompany Headline : "+str(company["headline"])+"\nCompany Subline: "+str(company["subline"])+"\n")
    #---------------------------------employee---------------------------------------------------------------------------#

    #Ici on va extraire une liste des gens qui travaillent dans une entreprise spÃ©cifique 
    #on demande au user de choisir une, ou plusieurs entreprises depuis la liste prÃ©cedentes, afin qu elles soient notre target pour la recherche
    print("Employees of this company are : \n")
    cpt_e=1
    l=[]
    l.append(str(company["urn_id"]))
    people_list=api.search_people(current_company=l)
for employee in people_list:
    l=employee["public_id"].split("-")
    print("************** employee number :"+str(cpt_e)+"******************")
    if(len(l)>1):
        print(l[0]+" "+l[1])
    else:
        print(l[0])
    cpt_e=cpt_e+1
    print("--------------------------jobs----------------------------")
    print("les offres disponilble pour :"+str(company["name"])+" sont : ")
    jobs=api.search_jobs(companies=str(company["name"]))
    cpt_j=1
for job in jobs:
    print("************** job number :"+str(cpt_j)+"******************")
    print("Job title : "+str(job["title"]))
    print("job location : "+str(job["formattedLocation"]))
    print("job workRemoteAllowed : "+str(job["workRemoteAllowed"]))
    cpt_j=cpt_j+1
    #--------------------------------------posts----------------------------------------#
    print("***************** posts******************")
    print(api.get_profile_posts(public_id=str(company["urn_id"]), urn_id=str(company["urn_id"]), post_count=10))
    cpt=cpt+1

#--------------------------------------------------------------------2---------------------------------------------------------------------------

"""
#18388752

#avoir la description , l'address , le site web d'une entrepreprise en utilisant son 

print(api.get_company("18388752"))

#--------------------------------------------------------------------3---------------------------------------------------------------------------#les offres d'emploi

print("--------------------------jobs----------------------------")

print(api.search_jobs(companies="echobox"))

#--------------------------------------------------------------------employee---------------------------------------------------------------------------#

    

#Ici on va extraire une liste des gens qui travaillent dans une entreprise spÃ©cifique 

#on demande au user de choisir une, ou plusieurs entreprises depuis la liste prÃ©cedentes, afin qu elles soient notre target pour la recherche

urn_ids=str(input("Recherche des employÃ©s, veuillez entrer une liste des urn_id des entreprises cibles (depuis la liste prÃ©cedente). Veuillez les sÃ©parer par des virgules !!!! :\n").strip()) 

urn_id_list=urn_ids.split(",") 

print(urn_id_list) 

people_list=api.search_people(keywords=None, connection_of=None, network_depths=None, current_company=urn_id_list, past_companies=None, nonprofit_interests=None, profile_languages=None, regions=None, industries=None, schools=None, contact_interests=None, service_categories=None, include_private_profiles=True, keyword_first_name=None, keyword_last_name=None, keyword_title=None, keyword_company=None, keyword_school=None, network_depth=None, title=None)

#ya bcp de parametre s pour la requete api.search_people ici j'ai utilisÃ© qlq parametres pour tester seulement

#print(people_list[0])

for i in people_list :

    print(i) 



'''

people_list=api.search_people(keywords=None, connection_of=None, network_depths=None, current_company=None, past_companies=None, nonprofit_interests=None, profile_languages=None, regions=None, industries=None, schools=None, contact_interests=None, service_categories=None, include_private_profiles=True, keyword_first_name=None, keyword_last_name=None, keyword_title=None, keyword_company="ooredoo", keyword_school=None, network_depth=None, title=None)

'''
profile_posts=api.get_profile_posts(public_id=None, urn_id='ACoAAC7AL_8B4ol3jsx1Mi3vGzUSmAXDszXHV08', post_count=1)

#print(profile_posts[0])

for i in range(0,len(profile_posts),1):

    print() """
