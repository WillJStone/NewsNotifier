from replit import db


def get_rss_urls():
    """
    Retrieves the RSS urls from the database. NOTE THAT THIS IS AND FOREVER SHOULD BE READONLY.
    """
    return db["rss_feeds"]
