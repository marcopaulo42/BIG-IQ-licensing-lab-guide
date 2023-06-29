import sphinx_rtd_theme

project = "VE Licensing with BIG-IQ Lab Guide"
copyright = ""
author = "Paul Teiber"
release = "0.0.1"

extensions = ["sphinx_rtd_theme"]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
# html_last_updated_fmt = "%Y-%m-%d %H:%M:%S"
html_last_updated_fmt = None
html_theme_options = {
    "display_version": False,
    "collapse_navigation": False,
    "titles_only": True,
}
html_show_sourcelink = False
html_show_copyright = False
html_show_sphinx = False

latex_elements = {
    "pointsize": "12pt",
}
