---
name: slide-architect
description: Build quote-driven Quarto/RevealJS discussion decks from articles, reports, and book chapters about AI in education. Use when creating, structuring, or improving a deck in this repo. Pulls direct quotes from the source, writes pithy titles and subtitles that summarize each quote, and sequences the quotes so the deck builds to the author's conclusion.
---

# SlideArchitect

Turn a source article into a short discussion deck that lets **the author speak**. The deck's job is to show the article's argument through the author's own words, in order, so that the audience reaches the author's conclusion by the last slide.

## Ground rules

1. **Quotes carry the content.** Every body slide is built around one direct quote (occasionally two that contrast). Quotes are verbatim. Trimming with an ellipsis (…) is fine; rewording is not. Do not "fix" the author's grammar or emphasis.
2. **Our words are only titles and subtitles.** The title (≤ 7 words) and subtitle (one short line) summarize the *point* of the quote in a pithy way. No AI-written paragraphs, explanatory bullets, invented examples, or "AI application" commentary on the slide. If the slide needs more than a title, subtitle, and quote to make sense, choose a better quote.
3. **One idea per slide.** One quote, one point.
4. **The deck holds together.** Titles read in sequence should tell the article's argument on their own. Each slide should set up the next one.
5. **Make the point clear early and land it at the end.** By slide 2 or 3 the audience should know the author's thesis (using the author's words). The final content slide is the author's conclusion.
6. **Don't change finished decks.** A folder that already has a rendered deck (`*.qmd` + `*.html` + `lead-slide.png`) is done. Leave its files alone unless the user asks for edits to that deck by name.
7. **Never commit source material.** PDFs and PNG screenshots of articles stay local (see `.gitignore`). Only `lead-slide.png` thumbnails are tracked.

## Folder layout

Each presentation lives in its own folder:

```
topic_folder/
├── <source>.pdf | IMG_*.PNG   # article PDF and/or highlighted screenshots (ignored by git)
├── quotes.md                  # key quotes, link to article at the top (tracked)
├── <slug>-slides.qmd          # the deck source (tracked)
├── <slug>-slides.html         # rendered, self-contained deck (tracked)
├── custom.scss                # deck theme (tracked)
├── lead-slide.png             # screenshot of the title slide; the index card thumbnail (tracked)
└── .gitignore                 # /.quarto/ and **/*.quarto_ipynb
```

**A new article** is a folder that has source material (PDF, screenshots, notes) but no `.qmd` deck yet. When asked to look for new work, list folders like that and start on them.

## Workflow

### Step 1: Gather requirements

Confirm, or assume these defaults when the user doesn't specify:

| Element | Default |
|---------|---------|
| **Folder** | The folder holding the source material |
| **Source** | The PDF, screenshots, or notes in that folder |
| **Purpose** | Discussion starter: show what the author argues |
| **Audience** | University faculty and administrators (BYU-Idaho) |
| **Tone** | The author's own; no added persuasion |
| **Length** | 8–14 slides including the title slide |

### Step 2: Read the source and build `quotes.md`

1. Read the full article. Some PDFs are image-only (`pdftotext` returns nothing); if so, render the pages (`pdftoppm -r 110 -png file.pdf out/p`) and read the images.
2. **Highlighted screenshots come first.** If the folder has screenshots with highlighted passages (e.g., `IMG_*.PNG` from a phone), those passages are the user's chosen key quotes. Every highlighted passage must appear in `quotes.md` and in the deck.
3. If there are no highlights, or not enough to carry the argument, choose quotes from the article that (a) state the thesis, (b) give the main evidence or examples, (c) mark turns in the argument, and (d) state the conclusion.
4. Write `quotes.md` in the folder using this template:

```markdown
# <Article title>

**<Author>**, *<Publication>*, <date>
[Read the article](<URL>)

## The point

> <The one quote that best states the article's thesis or conclusion>

## Key quotes

### 1. <Pithy title that summarizes the quote>
> "<verbatim quote>"

*Context:* <one line: where it appears / who is speaking, if not the author>
*Highlighted:* yes (IMG_1818.PNG)    ← only when it came from a screenshot
```

- The article link goes at the top. If the exact URL can't be confirmed (paywalled or blocked sites), use the publisher's search URL and mark it `<!-- TODO: replace with article URL -->`. Never invent a URL slug.
- List the quotes **in the order they appear in the article**. The deck may reorder them, but usually follows the article's order.
- Aim for 8–15 quotes. Include more than the deck uses so the user can swap them.

### Step 3: Outline the arc

Before writing the `.qmd`, write the sequence of slide titles only and check that the titles alone tell the story:

1. **Title slide.** Article title, with the article's subtitle/dek as the deck subtitle. Author and publication in `author`; article link in `institute`.
2. **The argument.** A three-part roadmap whose labels are the deck's sections, or the thesis quote itself.
3. **Setup.** The problem or situation, in the author's words.
4. **Body.** Evidence and turns in the argument, one quote per slide, each building on the last.
5. **Conclusion.** The author's closing claim as a quote, on a dark slide.
6. *(Optional)* **For discussion.** One question, clearly labeled as ours, that points back to the conclusion. No new claims.

### Step 4: Write the slides

For each body slide:

```markdown
## <Pithy title, ≤ 7 words>

<div class="subtitle-line"><one-line subtitle stating the point of the quote></div>

<div class="pull-quote">
<blockquote>"<verbatim quote>"</blockquote>
<div class="attribution">— <speaker, if not the author></div>
</div>

::: {.source-note}
<Author>, "<Title>," *<Publication>*, <date>.
:::

::: {.notes}
<The surrounding passage from the article, verbatim, so the presenter has the context.>
:::
```

**Titles and subtitles**
- The title is the claim, not the topic: "The credential no longer convinces," not "Credentials."
- Prefer the author's own memorable phrases for titles ("Going through the motions," "Who will step up?").
- The subtitle states in plain words what the quote shows. It must not add facts or opinions the article doesn't contain.
- Active voice, present tense, parallel structure across slides.

**Quotes**
- Verbatim, with curly quotes. Use an ellipsis for cuts, and square brackets only for unavoidable clarifications.
- Keep quotes to about 50 words or fewer on screen. Put the longer passage in the speaker notes.
- Highlight the key phrase in a long quote with `<span class="hl">…</span>`. Use at most one highlight per slide.
- Two quotes on one slide only when they contrast (e.g., product vs. process), using `.quote-pair`.

### Step 5: Render, screenshot, and register

1. Render: `quarto render <folder>/<slug>-slides.qmd` (decks use `embed-resources: true`).
2. Screenshot the title slide to `lead-slide.png` (1600×900) with headless Chrome:
   `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu --hide-scrollbars --window-size=1600,900 --screenshot=<folder>/lead-slide.png "file://$PWD/<folder>/<slug>-slides.html"`
3. Add a title-slide QR code that opens the deck (Short.io, domain shortie.fyi; the key is in the git-ignored `.env`, see `.env.example`):
   `uv run tools/shortio.py link https://byuistats.github.io/education_ai/<folder>/<slug>-slides.html --slug <short-slug> --title "<deck title>" --qr svg --out <folder>/assets/qr`
   Then put the snippet in the deck's `institute:` field (copy it from any other deck's `.qmd`; if the deck already has an article link, make `institute` a list) and add `@import "../tools/title-qr";` to the deck's `custom.scss`. Decks need an `author:` for `institute` to show. Verify the QR scans from `lead-slide.png`.
4. Register the deck: add an entry to `_data/decks.yml` (title from the deck, folder, html, qmd, `quotes: quotes.md`, date, type, source, slide count, topics, one-sentence description). The GitHub Pages index (`index.html`) is built from that file; don't edit the card markup. Also add a line to the slide deck sources list in `README.md`.
5. Add the folder's `.gitignore` (`/.quarto/` and `**/*.quarto_ipynb`).

### Step 6: Review

- [ ] Every highlighted passage from the screenshots appears in `quotes.md` and in the deck
- [ ] Every quote matches the source word for word (spot-check against the PDF)
- [ ] No slide contains our prose beyond the title, subtitle, and labels
- [ ] Reading only the titles tells the article's argument from start to finish
- [ ] The thesis is clear by slide 3; the last content slide is the author's conclusion
- [ ] Source note on every slide; article link on the title slide and in `quotes.md`
- [ ] No text overflows the slide at 1600×900 (check the rendered HTML)
- [ ] No PDFs or source screenshots are staged (`git status`)

## Other modes

### Update from audio or a speaker's text
1. Compare the audio or transcript with the slides.
2. Suggest slide updates based on what the speaker emphasized, keeping quotes verbatim.

### Improve an existing deck (only when asked by name)
1. Replace paraphrase with the source quote it summarizes.
2. Rewrite titles as pithy claims; cut explanatory bullets.
3. Reorder so the titles tell the argument.

## Theme direction

- **Typography.** Clean sans-serif for titles and labels; a serif for quotes so the author's voice stands apart from ours.
- **Colors.** 3–4 colors (primary, secondary, accent, neutral), defined as CSS variables in `custom.scss`.
- **Layout.** Quote large and left-aligned; title top-left; source note small at the bottom.
- **Contrast.** Dark text on a light background; dark background only for the thesis and conclusion slides.
- **Transitions.** Fade or none.
- **Size.** Quote text ≥ 28pt equivalent. If a quote doesn't fit, cut it with an ellipsis rather than shrinking the font.
