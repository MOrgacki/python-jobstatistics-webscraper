import requests
import string
import pymongo

try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    print("Connected successfully!!!")
except: 
    print("Could not connect to MongoDB")



mydb = myclient["mydatabase"]
mycol = mydb["customers"]

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

    for title in jobTitles:
        jobtitles_set.add(title['name'])

final_dictionary = dict.fromkeys(jobtitles_set, 0)
x = mycol.insert_one(final_dictionary)
print(jobtitles_set)

