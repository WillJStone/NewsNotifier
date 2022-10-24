"""
The main function of the program retrieves the urls from the database and uses the feedparser library to access the
RSS feeds. This process is repeated every n minutes.
"""


import feedparser

from src.utils import get_rss_urls


def main():
    rss_urls = get_rss_urls()
    for name, url in rss_urls.items():
        feed = feedparser.parse(url)
        print(f"Feed: {name}")
        for entry in feed.entries:
            print(f"Title: {entry.title}")
            print(f"Link: {entry.link}")
            print(f"Summary: {entry.summary}")
            print()
