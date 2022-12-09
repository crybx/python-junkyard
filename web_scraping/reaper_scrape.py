# python -m pip install requests
import requests
# python -m pip install beautifulsoup4
from bs4 import BeautifulSoup

chapter = "Chapter 55 - Conversation (2)"
url1 = "https://media.reaperscans.com/file"
url2 = "4SRBHm/comics/6512f39c-67dc-4de3-bdd1-92a84cfd6284/chapters/464de1d2-b825-48ca-81bb-90060cc39f92/"
url4 = ".jpg"
URL = ""
chapter_link_selectors = "ul > li > a"
title_selector = "h2"
content_selector = "article"
page = requests.get(URL)
print(page)
# print(page.text)
soup = BeautifulSoup(page.content, "html.parser")
chapter_links = soup.select(chapter_link_selectors)
print(chapter_links)
