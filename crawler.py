from bs4 import BeautifulSoup
from helpers.selenium_helper import SeleniumHelper
from locator import Locator
import datetime

class Crawler:

    def parse_html(self, content) -> BeautifulSoup:
        website_html = BeautifulSoup(content, "lxml")
        return website_html

    def scrape_job_tiles(self, job_tile, value_list):
        tile_header = job_tile.select(Locator.offer_title)
        if tile_header[0].name == "a":
            name = tile_header[0].text
            print(name)
            # items = job_tile.select(Locator.offer_items)
            company_name = job_tile.select_one(".offer-company__wrapper").text.replace('\n', '')
            print(company_name)
            rows = job_tile.select('.offer-labels__item')
            # for row in rows:
            #     print(row.text.replace('\n', ''))
            location = rows[0].text.replace('\n', '')
            print(location)
            # job offer view
            each_offer = {
                "name": name,
                "company_name": company_name,
                "location":location,
                "date_created":datetime.datetime.now()
            }
            value_list.append(each_offer)            
        elif tile_header[0].name == "button":
            #TUTAJ PODZIALAC
            offer_region = job_tile.select(".offer-regions")
            offer_region.select(".offer-regions__label").text
            print("Oferta wiele miast",  offer_region.select(".offer-regions__label").text)

    def parse_tiles(self,value_list, selenium_helper: SeleniumHelper, starting_page: int) -> list:
        selenium_helper.driver.get("https://www.pracuj.pl/praca" +
                                   "?pn=" + str(starting_page))
        offers_list_html = self.parse_html(
            selenium_helper.driver.page_source)
        job_tiles = offers_list_html('div', {'class': "offer"})

        for job_tile in job_tiles:
            self.scrape_job_tiles(
                 job_tile, value_list )

        return starting_page
