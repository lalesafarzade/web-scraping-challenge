from sre_constants import SUCCESS
import requests
import pandas
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time


url_list=['https://redplanetscience.com/',"https://spaceimages-mars.com",'https://galaxyfacts-mars.com/',"https://marshemispheres.com/"]


def scrape(url_list):
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    data_dict={}
    #NASA Mars News
    browser.visit(url_list[0])
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser') 
    element_ = soup.select_one("div.list_text")
    data_dict["news_title"]=element_.find("div", class_="content_title").get_text()
    data_dict["news_p"] =element_.find("div", class_="article_teaser_body").get_text()
    data_dict["news_date"]=element_.find("div", class_="list_date").get_text() 
    print("SUCCESS1") 
    #Featured Image
    browser.visit(url_list[1])
    time.sleep(3)
    browser.find_by_css('.fancybox-thumbs').click() 
    time.sleep(3)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial_img_url=soup.select_one("img.fancybox-image" ).get("src")
    data_dict["feuture_img_url"] = f"https://spaceimages-mars.com/{partial_img_url}"
    print("SUCCESS2") 


    tables = pd.read_html(url_list[2])
    df=tables[0]
    df.columns=df.iloc[0]
    df.drop(0,inplace=True)
    df.to_html('table.html')
    data_dict["tables"]=[df]
    print("SUCCESS3") 
    browser.visit(url_list[3])
    hemisphere_image_urls = []
    for item in range(4):
        hemisphere = {}
        browser.find_by_css("a.product-item h3")[item].click()
        sample_element = browser.links.find_by_text("Sample").first
        hemisphere["img_url"] = sample_element["href"]        
        hemisphere["title"] = browser.find_by_css("h2.title").text
        hemisphere_image_urls.append(hemisphere)  
        browser.back()
    data_dict["hemisphere_image_urls"]=hemisphere_image_urls
    print("SUCCESS4") 
    print(data_dict)
    return data_dict


scrape(url_list)