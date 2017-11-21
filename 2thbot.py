import feedparser
import time
from time import mktime, gmtime, strftime
import datetime

while(True):
	feed_url = "https://bato.to/myfollows_rss?secret=b9cd5daadbea4c3c0e941d8ded71ae45&l=English"
	feed = feedparser.parse(feed_url)
	first_item = feed["items"][0]
	print first_item
	dt = datetime.datetime.fromtimestamp(mktime(feed["items"][0]["published_parsed"]))
	title = feed
	if dt > datetime.datetime.now()-datetime.timedelta(seconds=59.99999):
		print # Post to reddit
	else:
		print # Don't post to reddit
	break
	time.sleep(60)
