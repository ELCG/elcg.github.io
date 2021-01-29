#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ezequiel Castaño'
SITENAME = 'Mi primer sitio'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'

TIMEZONE = 'America/Argentina/Cordoba'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

AUTHORS_SAVE_AS = 'autores/index.html'
CATEGORIES_SAVE_AS = 'categorias/index.html'
ARCHIVES_SAVE_AS = 'archivo/index.html'
TAGS_SAVE_AS = 'etiquetas/index.html'



ARTICLE_URL = 'posts/{slug}' 
ARTICLE_SAVE_AS = 'posts/{slug}/index.html'

PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'

AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}.html'

