from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time

START_URL = "https://exoplanets.nasa.gov/discovery/exoplanet-catalog/";

browser = webdriver.Chrome("/Users/sreelakshmi/Downloads/chromedriver");
browser.get(START_URL)
time.sleep(10)

def scrape():

    header = ["name", "light_years_from_earth", "planet_mass", "stellar_mag", "discovery_data"]

    planet_data =[]

    for i in range(0,452):

        soup = BeautifulSoup(browser.page_source, "html.parser")

        for ul_tags in soup.find_all("ul", attrs= ("class", "exoplanet")):
            li_tags = ul_tags.find_all("li")
            temp_list =[]

            #enumerate - ["a","b","c", "d"] --> (0,a), (1,b), (2,c), (3, d)

            for index, li_tag in enumerate(li_tags):
                if index ==0:
                    temp_list.append(li_tag.find_all("a")[0].contents[0])

                else:
                    try:
                        temp_list.append(li_tag.contents[0])

                    except:
                        temp_list.append("")

                print("line"+str(index));

            planet_data.append(temp_list)
            

        browser.find_element_by_xpath('//*[@id="primary_column"]/footer/div/div/div/nav/span[2]/a')

    with open("scaper_1.csv", "w") as f:
        csvwritter = csv.writer(f)
        csvwritter.writerow(header)
        csvwritter.writerows(planet_data)



scrape()








