from sre_constants import SUCCESS
import requests
import pandas
from splinter import Browser
from bs4 import BeautifulSoup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
import time




url_list=['https://redplanetscience.com/',"https://spaceimages-mars.com",'https://galaxyfacts-mars.com/',"https://marshemispheres.com/"]
def scrape():
    url_list=['https://redplanetscience.com/',"https://spaceimages-mars.com",'https://galaxyfacts-mars.com/',"https://marshemispheres.com/"]
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)
    data_dict={}
    #NASA Mars News
    browser.visit(url_list[0])
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser') 
    text = soup.select_one("div.list_text")
    img=soup.select_one("div.list_image")
    data_dict["news_title"]=text.find("div", class_="content_title").get_text()
    data_dict["news_p"] =text.find("div", class_="article_teaser_body").get_text()
    data_dict["news_date"]=text.find("div", class_="list_date").get_text() 
    data_dict['news_img']=img.find("img").get('src')
    print("SUCCESS1") 
    #Featured Image
    browser.visit(url_list[1])
    time.sleep(1)
    browser.find_by_css('.fancybox-thumbs').click() 
    time.sleep(1)
    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')
    partial_img_url=soup.select_one("img.fancybox-image" ).get("src")
    data_dict["feuture_img_url"] = f"https://spaceimages-mars.com/{partial_img_url}"
    print("SUCCESS2") 

    # Mars Facts
    tables = pd.read_html(url_list[2])
    df=tables[0]
    df.columns=df.iloc[0]
    df.drop(0,inplace=True)
    df.set_index('Mars - Earth Comparison' , inplace=True)
    #mars_df = df.to_html(index=False) 
    mars_df = df.to_html() 
    mars_df =mars_df.replace("\n", "")
    data_dict["tables"]=mars_df
    print("SUCCESS3") 



    # Mars Hemispheres
    browser.visit(url_list[3])
    
    for item in range(4):
        
        browser.find_by_css("a.product-item h3")[item].click()
        sample_element = browser.links.find_by_text("Sample").first
        data_dict[f"img_url_{item}"] = sample_element["href"]        
        data_dict[f"title_{item}"] = browser.find_by_css("h2.title").text
        browser.back()
        time.sleep(1)
    print("SUCCESS4") 

    browser.quit()
    print(data_dict)
    return data_dict
    

