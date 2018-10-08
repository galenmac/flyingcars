#DOC WITH MEG FOR FLYING CAR SCRAPE!

import time
from requests_html import HTMLSession

sesh = HTMLSession()

r = sesh.get("https://www.instructables.com/howto/flesh/")

#r.html.render()

# items = r.html.find("#resultsContainer")

items = r.html.find("div .explore-cover-item.cover-item >  .cover-info > .title")

print(items)
for item in items:
    print(item.text)
#items = r.html.find("a")
print(len(items))

#for item in items:
#        print(item.find("a"))
#print(len(items))
# for item in items:
#         # print(item)
#         tag = item.find("a", first = True)
#         url = "https://www.instructables.com"+(tag.attrs.get("href"))
#         r = session.get(url)
