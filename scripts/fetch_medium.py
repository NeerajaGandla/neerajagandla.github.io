import feedparser
import json

feed = feedparser.parse("https://medium.com/feed/@gaandlaneeraja")

posts = []

for entry in feed.entries[:6]:
    posts.append({
        "title": entry.title,
        "link": entry.link,
        "summary": entry.summary[:180].replace("<p>", "").replace("</p>", "")
    })

with open("latest-posts.json", "w", encoding="utf-8") as f:
    json.dump(posts, f, indent=4)
