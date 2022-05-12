from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
article_title = soup.find(name='a', class_='titlelink')
print(article_title.getText())
article_link = article_title.get('href')
print(article_link)
article_upvote = soup.find(name='span', class_='score')
print(article_upvote.getText())

# with open("website.html", encoding='utf-8') as file:
#     contents = file.read()

# soup = BeautifulSoup(contents, 'html.parser')
# # print(soup.title)
# # print(soup.title.string)
# #
# # print(soup.prettify())
#
# all_anchor_tags = soup.find_all(name='a')
# heading = soup.find(name='h1', id='name')
# # print(heading)
#
# section_heading = soup.find(name='h3', class_='heading')
# # print(section_heading)
#
# for tag in all_anchor_tags:
#     # print(tag.getText())
#     # print(tag.get("href"))
#     # print()
#     pass
#
# company_url = soup.select_one(selector='p a')
# print(company_url)