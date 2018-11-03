#!/usr/bin/env python3
import datetime

extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.mathjax',
    'sphinx.ext.githubpages',
]

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'
project = 'Айдеко Mesh'
author = 'Айдеко'
copyright = '%d, %s' % (datetime.datetime.now().year, author)

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1.0'
# The full version, including alpha/beta/rc tags.
release = '1.0'
language = 'ru'

html_theme = "sphinx_rtd_theme"
html_static_path = ['_static']
htmlhelp_basename = 'mesh'
# https://sphinx-rtd-theme.readthedocs.io/en/latest/
html_show_sourcelink = False
html_logo = '_static/mesh_full_logo.svg'
html_theme_options = {
    'display_version': False,
    'logo_only': True,
}

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'IdecoMesh.tex', project, author, 'manual'),
]
