#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Ezequiel Castaño'
SITENAME = 'Mi primer sitio'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = 'docs/'
THEME = "MinimalXY"

TIMEZONE = 'America/Argentina/Cordoba'

DEFAULT_LANG = 'es'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

PLUGIN_PATHS = ['plugins']
PLUGINS = [
    "sitemap", "shortener", "pelican-ert", "pelican.plugins.render_math", "bundler", "blur_thumbnails",
    "service_worker"
]

SERVICE_WORKER_THEMPLATE = "content/extra/sw_template.js"

STATIC_PATHS = ["images", "extra"]

EXTRA_PATH_METADATA = {
    'extra/icon-192x192.png': {'path': 'icon-192x192.png'},
    'extra/icon-256x256.png': {'path': 'icon-256x256.png'},
    'extra/icon-384x384.png': {'path': 'icon-384x384.png'},
    'extra/icon-512x512.png': {'path': 'icon-512x512.png'},
    'extra/manifest.webmanifest': {'path': 'manifest.webmanifest'},
}

BLUR_PATH = "content"

ERT_WPM = 200
ERT_FORMAT = "{time}"
ERT_INT = True

SHORTENER_FILE = "shortener.json"
SHORTENER_FOLDER = "link"

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.75,
        'indexes': 1,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}

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

