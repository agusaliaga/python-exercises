import urllib.request

term = "artificial intelligence"
page_number = 1
items_per_page = 20

u = urllib.request.urlopen("https://www.ted.com/search?page={}&per_page={}&q={}".format(page_number,items_per_page, term.replace(" ", "+")))
data = u.read()

from lxml import html
doc = html.document_fromstring(data)

for title in doc.cssselect("article.search__result h3 a"):
    print(title.text_content())


