import requests
import time

class RequestHelper:

    def get_jobtitle_amount(self, jobtitle):
        url = f"https://www.pracuj.pl/praca/count/all?ao=&jobicon=&kw={jobtitle}&oca=&p=0&rd=30&sal=&sc=0&ua=&wpl="
        headers = {
        'authority': 'www.pracuj.pl',
        'accept': 'application/json, text/plain, */*',
        'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.87 Safari/537.36',
        'sec-gpc': '1',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-mode': 'cors',
        'sec-fetch-dest': 'empty',
        'accept-language': 'en-US,en;q=0.9',
        }
        payload={}

        response = requests.request("GET", url, headers=headers, data=payload)
        amount = response.json()['offersCount'] + response.json()['jobCenterOffersCount']
        time.sleep(0.2) #anty cloudflare
        return amount

    def get_jobtitle(self, letter):
        url = f"https://massachusetts.pracuj.pl/suggestion?limit=999999999&query=+{letter}&dictionaries=jobTitles"
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
        payload= {}
        

        response = requests.request("GET", url, headers=headers, data=payload)
        jobTitles =  response.json()['jobTitles']
        time.sleep(0.2) #anty cloudflare
        return jobTitles
        