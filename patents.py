#DOC WITH MEG FOR FLYING CAR SCRAPE!

import time
from requests_html import HTMLSession

sesh = HTMLSession()

r = sesh.get("https://www.instructables.com/howto/flesh/")


flesh = []

# r.html.render()

items = r.html.find(".explore-cover-item")

for item in items:
        # print(item)
        tag = item.find("div span a")
        url = "https://www.instructables.com"+(tag[0].attrs.get("href"))
        r = sesh.get(url)
        title = r.html.find(".header-title")
        titleString = title[0].text
        # print(title[0].text)
        steps = r.html.find(".step-title")
        tempsteps = []
        for step in steps:
            tempsteps.append(step.text)
        flesh.append({"Title" : titleString, "Steps" : tempsteps})

for item in flesh:
    for key in item:
        print(item[key])
