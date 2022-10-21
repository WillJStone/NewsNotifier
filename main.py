import feedparser
#import rich

rss = feedparser.parse("http://rss.cnn.com/rss/cnn_topstories.rss")

print(rss.entries[0])
