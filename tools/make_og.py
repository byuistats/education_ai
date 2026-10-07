#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.9"
# dependencies = ["pyyaml"]
# ///
"""Write <folder>/og-header.html for every deck in _data/decks.yml.

These tags make a shared link (including shortie.fyi short links, which redirect to the deck) show
the deck's title, description, and title-slide image in Slack, Teams, iMessage, email, and social apps.
Each deck's .qmd lists og-header.html under format: revealjs: include-in-header.
Run after changing a deck's title or description:  uv run tools/make_og.py
"""
import html, yaml
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BASE = "https://byuistats.github.io/education_ai"
SITE = "AI in Education · BYU-Idaho Statistics"

for d in yaml.safe_load((ROOT / "_data/decks.yml").read_text()):
    e = lambda s: html.escape(str(s), quote=True)
    url = f"{BASE}/{d['folder']}/{d['html']}"
    img = f"{BASE}/{d['folder']}/lead-slide.png"
    tags = f'''<meta name="description" content="{e(d['description'])}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{e(SITE)}">
<meta property="og:title" content="{e(d['title'])}">
<meta property="og:description" content="{e(d['description'])}">
<meta property="og:url" content="{e(url)}">
<meta property="og:image" content="{e(img)}">
<meta property="og:image:width" content="1600">
<meta property="og:image:height" content="900">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(d['title'])}">
<meta name="twitter:description" content="{e(d['description'])}">
<meta name="twitter:image" content="{e(img)}">
'''
    (ROOT / d["folder"] / "og-header.html").write_text(tags)
    print("wrote", d["folder"] + "/og-header.html")
