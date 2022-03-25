from bs4 import BeautifulSoup
from selenium import webdriver

def newsReuters(url):
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(executable_path='chromedriver', options=options)

    target_url = url
    driver.get(target_url)

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'lxml')
    
    # if website's dev className is changed, find media-story-card ------- to troubleshoot
    elem = soup.find_all('div', class_='media-story-card__body__3tRWy')
    #elem = soup.find_all('div', class_='MediaStoryCard__body___29KVeF')
    #elem = soup.find('ul', class_='search-results__list___2A3hqM')

    # ----------------save 'a' tag for each news into groupedA----------------
    groupedA = []
    for i in elem:
        a = []
        for j in i.find_all("a"):
            a.append(j)
        groupedA.append(a)
    '''
    # debugging print statement
    print(groupedA[0])
    for i in groupedA[0]:
        print(i)
    '''
    # ----------------save article title and URL separately----------------
    hrefList = []
    titleList = []
    count = 0

    for i in groupedA:
        soup2 = BeautifulSoup(str(i), 'lxml')
        tmp = soup2.find('a')
        titleList.append(tmp.contents[0])   # title is added
        hrefList.append('https://www.reuters.com' + tmp.get('href')) #absolute link is added
        count += 1
    
    """
    # debugging print statement
    print("Debug: printing the list elements")
    for title in titleList:
        print("In title")
        print(title)
    for link in hrefList:
        print(link)
    """

    driver.quit()
    return titleList, hrefList
    

"""
# 'https://www.reuters.com/world/us/'
# 'https://www.reuters.com/site-search/?query=us'
usNewsTitle = newsReuters('https://www.reuters.com/site-search/?query=us')[0]
usNewsURL = newsReuters('https://www.reuters.com/site-search/?query=us')[1]
jpNewsTitle = newsReuters('https://www.reuters.com/site-search/?query=japan')[0]
jpNewsURL = newsReuters('https://www.reuters.com/site-search/?query=japan')[1]

for i in usNewsTitle:
    print(i)
for i in usNewsURL:
    print(i)

for i in jpNewsTitle:
    print(i)
for i in jpNewsURL:
    print(i)
"""