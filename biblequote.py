#!/usr/bin/env python3
# Title: Bible Verse
# Notes: Scrapes a Bible verse from a Bible quote web page.
#        This is just a test using BeautifulSoup and creating
#        a shell tool for fun. 
# Author: Robert Freiberger
# License: BSD
# Git: https://github.com/rfreiberger/Bible-Quote

import textwrap
import requests
from bs4 import BeautifulSoup

## variables
verseurl = "https://www.verseoftheday.com/"
versechapter = ""
versewords = ""

verseraw = requests.get(verseurl)
versesoup = BeautifulSoup(verseraw.text, 'html.parser')
versewords = ''.join(versesoup.find('p', class_='pfp-text').contents)

print("\n".join(textwrap.wrap(versewords, width=80, break_long_words=False)))
