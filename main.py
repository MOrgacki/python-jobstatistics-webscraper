import requests
import string
import pymongo
import datetime

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")



mydb = myclient["pracujPL"]
mycol = mydb["jobtitles"]

coll = myclient["local"]["test2"]

jobtitles_set = set()
alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

for letter in alphabet_list:
    url = f"https://massachusetts.pracuj.pl/suggestion?limit=999999999&query=+{letter}&dictionaries=jobTitles"
    payload= {}
    headers = {
        'authority': 'massachusetts.pracuj.pl',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
        'sec-gpc': '1',
        'origin': 'https://www.pracuj.pl',
        'sec-fetch-site': 'same-site',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'referer': 'https://www.pracuj.pl/',
        'accept-language': 'en-US,en;q=0.9',
        }

    response = requests.request("GET", url, headers=headers, data=payload)

    jobTitles =  response.json()['jobTitles']
    
    # print(jobTitles)
    # for title in jobTitles:
    #     jobtitles_set.add(title['name'])

    final_list = []
    for key in jobTitles:
            if len(list(mycol.find({'name': key['name']}))) > 0:
                mycol.update_one(filter = {'name': key['name']},replacement={"date_updated": datetime.datetime.now()}, upsert=True)
            else:
                each_jobTitle = {
                    "external_id": key['id'],
                    "name": key['name'],
                    "date_created":datetime.datetime.now(),
                    "date_updated":datetime.datetime.now()
                }
                print({"name": each_jobTitle['name']})
                x = mycol.replace_one(filter = {"name": each_jobTitle['name']},replacement=each_jobTitle, upsert=True)



