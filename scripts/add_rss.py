import argparse
import sys

from replit import db


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("url", help="URL of RSS feed")
    parser.add_argument("name", help="Name of RSS feed")

    return parser.parse_args(sys.argv[1:])


def add_rss(url: str, name: str):
    db["rss_feeds"][name] = url


def main():
    args = parse_args()
    add_rss(args.url, args.name)


if __name__ == "__main__":
    main()
