

import request
import requests
from bs4 import BeautifulSoup

r = requests.get("https://en.wikipedia.org/wiki/Naive_Bayes_spam_filtering")
print(r.text)

# Remove html tags
soup = BeautifulSoup(r.text, "html5lib")
print(soup.get_text())

summaries=[]
for i in soup.find_all("li"):
  if not i.find(class_='mwe-math-element'):
        summaries.append(i)
summaries

summaries[0].find("a").get_text().strip()

articles=[]
for i_article in summaries:
 
  try:
    articles.append(i_article.find("a").get_text().strip())
  except:
    continue
articles
