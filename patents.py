#DOC WITH MEG FOR FLYING CAR SCRAPE!

import time
from requests_html import HTMLSession

sesh = HTMLSession()

r = sesh.get("https://patents.google.com/?q=(flying+car)&oq=(flying+car)")

r.html.render()

# items = r.html.find("#resultsContainer")

items = r.html.find("div .search-results")

print(items)
# for item in items:
#         # print(item)
#         tag = item.find("a", first = True)
#         url = "https://www.instructables.com"+(tag.attrs.get("href"))
#         r = session.get(url)
