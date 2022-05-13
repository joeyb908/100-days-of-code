from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")
articles = soup.find_all(name='a', class_='titlelink')

article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.get('href')
    article_links.append(link)

print(article_texts)
print(article_links)

article_upvotes = [score for score in soup.find_all(name='span', class_='score')]
print(article_upvotes)
#article_upvotes = soup.find_all(name='span', class_='score')


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