from bs4 import BeautifulSoup
import requests

def scraping(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "lxml")
    res = soup.findAll('h1', {'class': 'pageMainHeadingWrapper newsCardMainHeading'})
    for headline in res:
        print("Headlines: {}".format(headline.text.strip()))
    auth = soup.findAll('a', {'class': 'linkColorRed'})
    print("Name of author: {}".format(auth[2].get('title')))
    time = soup.find(class_='contentWidthNewcIteamCard')
    print("time of publish: {}".format(time.text))
    summary_elements = soup.find(class_="story-summary")
    print("Summary: {}".format(summary_elements.text))
    
    # Content
    content = soup.find_all(class_='newsDiscription')
    for i in content:
        if i.name == 'h2':
            print("Heading: {}".format(i.text.strip()))
        else:
            print(i.text.strip())

main_url = 'https://telugu.hindustantimes.com/rss/telangana'
main_res = requests.get(main_url)
main_soup = BeautifulSoup(main_res.content, 'xml')
eachlink = []
Alllinks = main_soup.findAll('link')
for link in Alllinks:
    eachlink.append(link.text)

cleanlinks = eachlink[3:]
print(cleanlinks)

for i in cleanlinks:
    scraping(i)
    for j in range(15):
        print(":")

