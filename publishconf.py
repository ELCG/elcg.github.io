#!/usr/bin/env python
# -*- coding: utf-8 -*- #

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

# If your site is available via HTTPS, make sure SITEURL begins with https://
SITEURL = 'https://elcg.github.io'
RELATIVE_URLS = False

GOOGLE_ANALYTICS = "G-G194ENC3CE"
DISQUS_SITENAME = "https-elcg-github-io"

FEED_DOMAIN = 'http://feeds.feedburner.com'
FEED_ALL_ATOM  = 'ELCG'
FEED_ATOM  = 'feeds/all.atom.xml'


RECORD_SESSION = False

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""