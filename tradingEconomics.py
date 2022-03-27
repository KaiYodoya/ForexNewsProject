from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# The program returns the list of news title and list of news link
# index will correspond each other
# precondition: url is the news top page
# post condition:   retrieveInfo[0] returns the list of news link
#                   retrieveInfo[1] returns the title of news
def newsTradingEconomics(url):
    opts = Options()
    opts.headless = True
    opts.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(options=opts)

    target_url = url
    driver.get(target_url)

    html = driver.page_source.encode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')

    elems = soup.find('div', id='stream')

    # separate each news into each element of list so I can handle one by one
    groupedA = []
    for i in elems.find_all("li"):
        #print(i)
        a = []
        for j in i.find_all("a"):
            a.append(j)
        groupedA.append(a)
    # Now, groupedA[] has all the tag of one news.
    # All the important info is at the position of groupedA[][2]


    # -------------------I need the elements with separate lists-------------------------------
    hrefList = []
    titleList = []
    count = 0
    # print(groupedA[2])    # <- run this to see what is inside 
    for i in groupedA:  # groupedA[2] has 'a' tag of one news that all information is inside
        
        titleList.append(i[2].b.string) # append title

        soup2 = BeautifulSoup(str(i[2]), 'html.parser')
        tmpA = soup2.find('a')
        hrefList.append('https://tradingeconomics.com' + tmpA.get('href')) # append absolute link

        groupedA[count] = i[2]
        count += 1
    
    #for i in range(len(hrefList)):
        #print(hrefList[i], '\t', titleList[i])

    driver.quit()
    return titleList, hrefList

"""
#newsTradingEconomics('https://tradingeconomics.com/japan/news')
usNewsTitle = newsTradingEconomics('https://tradingeconomics.com/united-states/news')[0]
usNewsURL = newsTradingEconomics('https://tradingeconomics.com/united-states/news')[1]

for i in usNewsTitle:
    print(i)
for i in usNewsURL:
    print(i)
"""