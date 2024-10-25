import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

def main():
    url = "https://montrealgazette.com/category/news/"
   
    
    options =Options()
    options.add_argument('--headless')  # Run in headless mode
    options.add_argument('--no-sandbox')
    
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")

    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")

   
    driver=webdriver.Chrome(options=options)
    driver.get(url)
    
    driver.implicitly_wait(5) 
    html_text = driver.page_source
    
    soup = BeautifulSoup(html_text,"html.parser")

    # grab headlines

    headlines = soup.find_all('span', attrs={'data-tb-title': True, 'class': 'article-card__headline-clamp',
                                             'data-tb-shadow-region-title': '0'})
                                            # 'data-tb-owning-region-name':'Main'})
    
    #class2_elements = soup.find_all(class_='article-card article-card--no-category-top article-card--small-padlock', attrs={'data-tb-owning-region-name':'Main'})
    #class2_elements = [element for element in soup.find_all(class_='article-card article-card--no-category-top article-card--small-padlock') if element.get('data-tb-owning-region-name') == 'Main']

    for e in headlines:
        print(e.text)
        
    
    
    
if __name__ == "__main__":
     main()