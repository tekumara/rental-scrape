#!/usr/bin/env python

from bs4 import BeautifulSoup
import requests
import argparse

def scrape(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, features="html.parser")

    price = soup.find("div", id="PriceSummaryDetails_TitlePrice").contents[0]
    list_date = soup.find("div", id="PriceSummaryDetails_ListedStatusText").contents[0]

    table = soup.find("table", id="ListingAttributes")
    location = table.tr.td.contents[0]
    desc = soup.find("div", id="ListingDescription_ListingDescription")

    print(price)
    print(list_date)
    print(location)
    print(desc)

def main():
    parser = argparse.ArgumentParser(description="Scrape rental data from trademe",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('url', help="url")
    args = parser.parse_args()
    scrape(args.url)


if __name__ == "__main__":
    main()



