# Configuration file for the Sphinx documentation builder.

import os
import sys
from datetime import date
#import ablog

# Project information
project = 'HoldTheDoor'
copyright = '2024, HoldTheDoor'
author = 'HoldTheDoor'
release = '1.0.0'

# Insert '_extension' directory into the path so Sphinx can find it
sys.path.insert(0, os.path.abspath('_extension'))
sys.path.insert(0, os.path.abspath('scripts'))

html_baseurl = 'https://holdthedoor.ca/'
html_extra_path = ['robots.txt']

# General configuration
extensions = [
    'myst_parser',
    'sphinx_design', 
    'gallery_directive',
    'component_directive',
    'ablog',
    'sphinx.ext.autodoc',
    'sphinx.ext.intersphinx',
    'sphinx_togglebutton',
    'sphinx_favicon',
    'sphinxcontrib.youtube',
    'sphinx.ext.autosectionlabel',
    'split_articles',
    'sphinx_sitemap'
]

autosectionlabel_prefix_document = True

# Path configurations
templates_path = ["_templates"]
html_static_path = ["_static"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

# MyST options
myst_enable_extensions = ["colon_fence", "linkify", "substitution"]
myst_heading_anchors = 2
myst_substitutions = {"rtd": "[Read the Docs](https://readthedocs.org/)"}

# ABlog settings
blog_basepath = 'news'
blog_path = 'news'
blog_post_pattern = 'news/articles/*/*/*.rst'
blog_feed_fulltext = True
blog_feed_subtitle = "Latest News and Updates"

blog_posts_per_page = 5
paginate_archived_posts = True

# Post related settings
post_auto_excerpt = 1
post_date_format = '%Y-%m-%d'
post_date_format_short = '%B %d, %Y'




# HTML output options
html_theme = "pydata_sphinx_theme"
html_logo = "_static/logo.svg"
html_favicon = "_static/favicon.ico"
html_title = "We Hold The Door Open to Canada for You!"

html_theme_options = {
    "external_links": [
    ],
    "icon_links": [
        {"name": "X", "url": "https://x.com/holdthedoor_ca", "icon": "fa-brands fa-x-twitter"},
        {"name": "Email", "url": "mailto:holdthedoor.ca@gmail.com", "icon": "fa-solid fa-envelope"},
    ],
    "logo": {
        "text": "HoldTheDoor.ca",
        "image_dark": "_static/logo-dark.svg",
    },
    "show_toc_level": 1,
    "navbar_align": "left",
    "show_version_warning_banner": False,
    "footer_start": "",
    "footer_end": ["copyright"],
    "secondary_sidebar_items": ["page-toc", "aboutus"   ],

}

# Sidebar configuration
html_sidebars = {
    "**": ["sidebar-nav-bs", "custom-template", "sidebar-ethical-ads"],
    "index": [],
    "visitor/index": [],
    "immigration/index": [],
    "citizen/index": [],
    "news/index": [],
    "officialwebsites/index": [],
}


html_context = {
    "doc_path": "docs",
    "title": "HoldTheDoor"
}

# Custom styles and scripts
html_css_files = ["custom.css"]
html_js_files = ["pydata-icon.js", "custom-icon.js", "google_analytics.js"]
todo_include_todos = True

# Favicon configuration
favicons = [
    "favicon-32x32.png",
    "favicon-16x16.png",
    {"rel": "shortcut icon", "sizes": "any", "href": "favicon.ico"},
    "android-chrome-192x192.png",
    {"rel": "mask-icon", "color": "#459db9", "href": "safari-pinned-tab.svg"},
    {"rel": "apple-touch-icon", "href": "apple-touch-icon.png"},
    {"name": "msapplication-TileColor", "content": "#459db9"},
    {"name": "theme-color", "content": "#ffffff"},
    {"name": "msapplication-TileImage", "content": "mstile-150x150.png"},
]