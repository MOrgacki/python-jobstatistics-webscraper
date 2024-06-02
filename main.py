import requests
import string
import datetime
import helpers.mongo_helper as mongo
from helpers.selenium_helper import SeleniumHelper
from selenium.webdriver.remote.webdriver import WebDriver
import requests

from selenium.webdriver.support.ui import WebDriverWait
from crawler import Crawler
from locator import Locator
from selenium.webdriver.support import expected_conditions as EC
import time
import helpers.requests_helper as req

#Class Objects
crawler = Crawler()
mongo_helper = mongo.MongoHelper()
request_helper = req.RequestHelper()

def assign_cookies(selenium: WebDriver):
    cookies = selenium.get_cookies()
    request = requests.Session()
    for cookie in cookies:
        request.cookies.set(cookie['name'], cookie['value'])
    return request


def run_jobTitles():
    #Letters
    alphabet_string = string.ascii_uppercase
    alphabet_list = list(alphabet_string)

    for letter in alphabet_list:
        jobTitles = request_helper.get_jobtitle(letter)
        for key in jobTitles:
                if len(list(mongo_helper.mycol.find({'name': key['name']}))) > 0:
                    offer_amount = request_helper.get_jobtitle_amount(key['name'])
                    mongo_helper.mycol.update_one(filter = {'name': key['name']},update={"$set": {"offers_amount": offer_amount, "date_updated": datetime.datetime.now()}}, upsert=False)
                else:
                    offer_amount = request_helper.get_jobtitle_amount(key['name'])
                    each_jobTitle = {
                        "external_id": key['id'],
                        "name": key['name'],
                        "offers_amount":offer_amount,
                        "date_created":datetime.datetime.now(),
                        "date_updated":datetime.datetime.now()
                    }
                    print("Added: "+ each_jobTitle['name'])
                    mongo_helper.mycol.replace_one(filter = {"name": each_jobTitle['name']},replacement=each_jobTitle, upsert=True)

def run_offers():
    selenium_helper = SeleniumHelper()
    try:
        selenium_helper.login(
            "YOUR_EMAIL", "YOUR_PASSWORD", "https://login.pracuj.pl")
        selenium_helper.cookies_handler()
        session = assign_cookies(selenium_helper.driver)
        time.sleep(5)
        selenium_helper.driver.get("https://www.pracuj.pl/pracuj")
        WebDriverWait(driver=selenium_helper.driver, timeout=10).until(
            EC.title_contains(("Oferty pracy")))
    except:
        print("Cant pass login phase")
    
    offers_list_html = crawler.parse_html(selenium_helper.driver.page_source)
    # count pages
    value_list = []
    temp_nr = offers_list_html.select(Locator.pagination_number)
    page_nr = int(temp_nr[0].next_element.replace('\n', ''))
    #tutaj trzeba fixnac srodek
    page_nr = range(1, page_nr+1, 1)
    mongo_helper.mycol2.delete_many( { } )
    for starting_page in page_nr:
        print("Page number: ", starting_page)
        start = time.time()
        crawler.parse_tiles(
            value_list, selenium_helper, starting_page)
        end = time.time()
        print(f"Page numer {starting_page} took:",
              (end - start)/60, 'min.')
        page = session.get("https://www.pracuj.pl/pracuj" + "?pn=" +
                           str(starting_page))
        offers_list_html = crawler.parse_html(page.content)
    mongo_helper.mycol2.insert_many(value_list)

def main():
    run_jobTitles()
    # run_offers()

if __name__ == "__main__":
    main()
