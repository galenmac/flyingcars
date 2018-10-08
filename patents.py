#DOC WITH MEG FOR FLYING CAR SCRAPE!

import time
from requests_html import HTMLSession

sesh = HTMLSession()

r = sesh.get("https://www.instructables.com/howto/flesh/")

# r.html.render()

items = r.html.find(".explore-cover-item")

for item in items:
        # print(item)
        tag = item.find("a", first = True)
        url = "https://www.instructables.com"+(tag.attrs.get("href"))
        r = sesh.get(url)
        steps = r.html.find(".step-title")
        for step in steps:
            print(step.text)
