# (C) British Crown Copyright 2010 - 2015, Met Office
#
# This file is part of Iris.
#
# Iris is free software: you can redistribute it and/or modify it under
# the terms of the GNU Lesser General Public License as published by the
# Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Iris is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Iris.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import (absolute_import, division, print_function)
from six.moves import (filter, input, map, range, zip)  # noqa

# -*- coding: utf-8 -*-
#
# Iris documentation build configuration file, created by
# sphinx-quickstart on Tue May 25 13:26:23 2010.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
sys.path.append(os.path.abspath('sphinxext'))

# add some sample files from the developers guide..
sys.path.append(os.path.abspath(os.path.join('developers_guide')))


# -- General configuration -----------------------------------------------------

# Temporary value for use by LaTeX and 'man' output.
# Deleted at the end of the module.
_authors = ('Byron Blay', 'Ed Campbell', 'Philip Elson', 'Richard Hattersley',
            'Bill Little')

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.coverage',
              'sphinx.ext.pngmath',
              'sphinx.ext.autosummary',
              'sphinx.ext.graphviz',
              'sphinx.ext.intersphinx',
              'sphinx.ext.doctest',
              'matplotlib.sphinxext.mathmpl',
              'matplotlib.sphinxext.only_directives',
              'matplotlib.sphinxext.plot_directive',

              # better class documentation
              'custom_class_autodoc',

              # Data instance __repr__ filter.
              'custom_data_autodoc',

              'gen_example_directory',
              'generate_package_rst',
              'gen_gallery',

              # Add labels to figures automatically
              'auto_label_figures',
              ]

# list of packages to document
autopackage_name = ['iris']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'contents'

# General information about the project.
project = u'Iris'
# define the copyright information for latex builds. Note, for html builds,
# the copyright exists directly inside "_templates/layout.html"
copyright = u'British Crown Copyright 2010 - 2015, Met Office'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
import iris
# The short X.Y version.
if iris.__version__ == 'dev':
    version = 'dev'
else:
    # major.feature(.minor)-dev -> major.minor
    version = '.'.join(iris.__version__.split('-')[0].split('.')[:2])
# The full version, including alpha/beta/rc tags.
release = iris.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['sphinxext', 'build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# Definer the default highlight language. This also allows the >>> removal
# javascript (copybutton.js) to function.
highlight_language = 'python'

# A list of ignored prefixes for module index sorting.
modindex_common_prefix = ['iris']

intersphinx_mapping = {
   'python': ('http://docs.python.org/2.7', None),
   'numpy': ('http://docs.scipy.org/doc/numpy/', None),
   'scipy': ('http://docs.scipy.org/doc/scipy/reference/', None),
   'matplotlib': ('http://matplotlib.org/', None),
   'cartopy': ('http://scitools.org.uk/cartopy/docs/latest/', None),
   'biggus': ('http://biggus.readthedocs.org/en/latest/', None),
}


# -- Doctest ------------------------------------------------------------------

doctest_global_setup = 'import iris'

# -- Autodoc ------------------------------------------------------------------

autodoc_member_order = 'groupwise'
autodoc_default_flags = ['show-inheritance']

# include the __init__ method when documenting classes
# document the init/new method at the top level of the class documentation rather than displaying the class docstring
autoclass_content='init'

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  Major themes that come with
# Sphinx are currently 'default' and 'sphinxdoc'.
html_theme = 'default'
html_theme = 'sphinxdoc'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {'index': 'index.html', 'gallery':'gallery.html'}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = False

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# If nonempty, this is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = ''

# Output file base name for HTML help builder.
htmlhelp_basename = 'Irisdoc'

html_use_modindex = False


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
#latex_paper_size = 'letter'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('contents', 'Iris.tex', u'Iris Documentation', ' \\and '.join(_authors), 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
#latex_preamble = ''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True
latex_elements = {}
latex_elements['docclass'] = 'MO_report'

# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'iris', u'Iris Documentation', _authors, 1)
]

##########################
# plot directive options #
##########################

plot_formats = [('png', 100),
                #('hires.png', 200), ('pdf', 250)
                ]





# Delete the temporary value.
del _authors
