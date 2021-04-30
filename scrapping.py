from bs4 import BeautifulSoup, Tag
import requests
import json
url = 'https://www.udemy.com/featured-topics/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers)

soup = BeautifulSoup(response.content, 'html.parser')

# Sections
for script in (soup.find_all('script')):
    s:Tag = script
    if s.string is not None and "navigation_categories" in s.string:
        firstmatch = s.string.find("navigation_categories")
        content = (s.string[s.string.find("navigation_categories")+23:s.string.find("popular_subcategory_topics")])

        content = (content.strip()[:-1])

        content_json = json.loads(content)


        #print(json.loads(content))
        #print(s.string)
        #print(content)

