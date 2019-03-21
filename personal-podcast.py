#!/usr/bin/env python3
import os
import datetime
from feedgen.feed import FeedGenerator

###########
# OPTIONS #
###########

# maximum number of items to keep
MAX_ITEMS = 20
# whether to delete old items
DELETE_OLD = True
# location of audio files
PODCAST_DIR = "/var/www/html/podcast/"
# location of PODCAST_DIR on the internet
SERVER = "http://your-site.com/podcast/"
# title of podcast
TITLE = "Personal Podcast"
# description of podcast
DESC = "A personal podcast"
# podcast logo, as a url
LOGO = "http://placekitten.com/500/500"

os.chdir(PODCAST_DIR)
items = filter(lambda x: os.path.isfile(x) and x.endswith(".mp3"), os.listdir())
items = [f for f in items]
# sort by date, newest to oldest
items.sort(key=os.path.getmtime, reverse=True)

# delete items above max
if DELETE_OLD:
    for delete in items[MAX_ITEMS:]:
        print("DELETING: " + delete)
        os.remove(delete)

# keep only MAX_ITEMS newest items, reverse to be oldest to newest
items = items[:MAX_ITEMS][::-1]

fg = FeedGenerator()
fg.load_extension("podcast")
fg.title(TITLE)
fg.description(DESC)
fg.author({"name": "Rayquaza01"})
fg.link(href=SERVER + "podcast.rss", rel="self")
fg.logo(LOGO)
fg.podcast.itunes_image(LOGO)

# add entries
for item in items:
    fe = fg.add_entry()
    url = SERVER + urllib.parse.quote(item)
    fe.id(url)
    fe.published(datetime.datetime.fromtimestamp(os.path.getmtime(item), tz=datetime.timezone.utc))
    fe.title(item)
    fe.description(url)
    fe.enclosure(url, 0, "audio/mpeg")

# export to rss
fg.rss_str(pretty=True)
fg.rss_file("podcast.rss")
