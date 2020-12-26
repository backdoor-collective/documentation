import pkg_resources
from datetime import date
import sphinx_material
import recommonmark
from recommonmark.transform import AutoStructify

docs_version = "0.1.0"

# General information about the project.
project = "Backdoor Collective"
copyright = "{year}, Backdoor Collective".format(year=date.today().year)
version = release = docs_version

# Warn about missing references
nitpicky = True

# The suffix of source filenames.
"""
source_suffix = {
    ".rst": "restructuredtext",
    ".txt": "restructuredtext",
    ".md": "markdown",
}
"""
source_suffix = ['.rst', '.md']

exclude_patterns = []

extensions = [
    "sphinx_material",
    "sphinx.ext.doctest",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "recommonmark",
    ]

autosectionlabel_prefix_document = True
todo_include_todos = True


# -- Options for HTML output ----------------------------------------------
html_theme = 'sphinx_material'
html_static_path = ['_static']


# -- Options for Sphinx Material theme ---------------------------------------

html_show_sourcelink = True
html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}

# Required theme setup
html_theme_path = sphinx_material.html_theme_path()
html_context = sphinx_material.get_html_context()
html_logo = '_static/img/backdoor-collective-logo.png'

# Material theme options (see theme.conf for more information)
html_theme_options = {

    # Set the name of the project to appear in the navigation.
    'nav_title': project,

    # Specify a base_url used to generate sitemap.xml. If not
    # specified, then no sitemap will be built.
    'base_url': 'https://backdoor-collective.org/docs/',

    # Set the color and the accent color
    #'color_primary': '#000000',
    #'color_primary': 'blue',
    'color_primary': 'blue-grey',
    #'color_primary': 'grey',
    #'color_primary': 'indigo',
    #'color_primary': 'light-blue',
    #'color_accent': 'light-green',
    #'color_accent': 'light-blue',

    # Set the repo location to get a badge with stats
    'repo_url': 'https://github.com/backdoor-collective/documentation',
    'repo_name': 'documentation',

    # Visible levels of the global TOC; -1 means unlimited
    'globaltoc_depth': 1,
    # If False, expand all TOC entries
    #'globaltoc_collapse': False,
    # If True, show hidden TOC entries
    'globaltoc_includehidden': True,

    "master_doc": False,
    "nav_links": [
    ],

    "heroes": {
        #"index": "Foobar.",
        #"pages/cli": "On your fingertips.",
    },

    #"logo_icon": "https://avatars1.githubusercontent.com/u/74402891?s=80",
}


# ---


def setup(app):

    # Custom stylesheet.
    app.add_css_file("css/backdoor-collective-sphinx.css")

    # Configure recommonmark.
    app.add_config_value('recommonmark_config', {
            #'url_resolver': lambda url: github_doc_root + url,
            'enable_auto_toc_tree': True,
            'auto_toc_tree_section': 'Content',
            #'enable_auto_doc_ref': True,
            'enable_math': False,
            'enable_inline_math': False,
            'enable_eval_rst': True,
            }, True)
    app.add_transform(AutoStructify)
