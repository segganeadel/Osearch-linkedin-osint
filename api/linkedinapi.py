from linkedin_api import Linkedin
import json

api = Linkedin('selmaosint@gmail.com', '#Osint-2022')

company = api.get_company("djezzy")
j = json.dumps(company) 
print(j)

