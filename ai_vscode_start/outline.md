# AI with VS Code: Starting from Zero (deck outline)

**Working title:** Your First Day with AI in VS Code
**Subtitle:** Nothing installed yet? Start here.
**Audience:** BYU-Idaho faculty and staff with no programming tools on their computer (Mac or Windows)
**Goal:** By the end, the audience has VS Code, an AI assistant, and a small set of command-line tools running on their machine, and has watched the AI use those tools to build and check a real file.
**Type / group:** Workshop · Setup & training
**Length:** 21 main slides plus a backup section, a Claude appendix, and 11 tool profile slides; 45 to 60 minutes live
**Relationship to other decks:** This deck is the on-ramp. [Codex at BYU-I](../ai_codex/ai-codex-setup-slides.qmd) covers account sign-in and the Codex connection in detail, so this deck links to it instead of repeating it.

## Assumptions to confirm

- The AI assistant is **Codex** (OpenAI extension), since BYU-I provides ChatGPT access. Claude is covered in appendix slides, so the main path stays Codex-only.
- Audience can install software on their own computer. No admin-rights or "ask IT" slide.
- Mac and Windows are both shown. Slides show the one-line command for each; longer steps go in backup slides.
- Many attendees have no GitHub account, so account creation is its own pair of slides (15–16), not a backup.
- Format is a live follow-along: each setup slide ends with a "you should see…" check.
- Playwright is installed through uv (`uvx playwright install chromium`), so Node is not needed for it. Node stays in the set because many AI tools expect it.

## Tool set

| # | Tool | Why the AI needs it | Check |
|---|------|---------------------|-------|
| 1 | Package manager: [Homebrew](https://brew.sh) (Mac), [winget](https://learn.microsoft.com/windows/package-manager/winget/) (Windows) | Lets the AI install the rest | `brew --version` / `winget --version` |
| 2 | [Git](https://git-scm.com) | Shows what the AI changed and lets you undo it | `git --version` |
| 3 | [uv](https://docs.astral.sh/uv/) | Installs and manages Python, so no separate Python installer | `uv --version` |
| 4 | [Quarto](https://quarto.org) | Turns text into slides, documents, and sites | `quarto --version` |
| 5 | [Playwright](https://playwright.dev) (Chromium) | Lets the AI open a page and screenshot it to check its own work | `uvx playwright --version` |
| 6 | [Node.js](https://nodejs.org) (LTS) | Runs many AI tools and MCP servers | `node --version` |
| 7 | [GitHub CLI](https://cli.github.com) (`gh`), with a free [GitHub account](https://github.com/signup) | Publishing and pull requests without passwords | `gh --version`, `gh auth status` |
| *Backup* | [rig](https://github.com/r-lib/rig) (R Installation Manager) | Installs and switches R versions, the R counterpart to uv | `rig --version` |

Also used, not part of the toolbox: [VS Code](https://code.visualstudio.com), the [Codex extension](https://marketplace.visualstudio.com/items?itemName=OpenAI.chatgpt), and the BYU-I [ChatGPT access page](https://www.byui.edu/ai/tools/chatgpt).

Left out on purpose: Docker, WSL, conda/Anaconda. Add by audience: R through rig (statistics faculty; backup slide), TinyTeX for PDF (`quarto install tinytex`).

## Arc

Titles read in order: *You don't need to be a programmer → Three things we'll install → Get VS Code → Open a folder → Add the AI → Sign in → Give it a toolbox → Install each tool → Make a GitHub account → Connect it → Let the AI check its own toolbox → Build a page and see it → You stay in charge → Keep going.*

## Slide outline

### Part 1: Why and what

1. **Title.** Your First Day with AI in VS Code. *Nothing installed yet? Start here.*
2. **You don't need to be a programmer.** AI in an editor can read, write, and change files, and run tools for you. Today is about getting set up, not learning to code.
3. **What we'll set up.** (1) VS Code, the editor; (2) the AI assistant, the helper; (3) a toolbox of command-line tools, the helper's hands. Show the finished screen as the target.

*Each slide that installs a tool has a small "What is this?" link next to the tool name that jumps to its profile in Appendix B (see below).*

### Part 2: Install and open

4. **Download VS Code.** code.visualstudio.com. Pick the Mac or Windows installer. Screenshot of the download page.
5. **Install it.** Mac: drag to Applications, open. Windows: run installer, accept defaults and keep "Add to PATH" checked. *Check: the welcome screen opens.*
6. **Tour in 60 seconds.** Sidebar, editor, terminal, command palette. Name only the four things we'll use. Command palette: Mac `cmd + shift + P`, Windows `ctrl + shift + P`.
7. **Make a project folder.** Create `ai-practice` in Documents, then File → Open Folder. Choose "Yes, I trust the authors." *Check: the folder name shows in the sidebar.*

### Part 3: Add the AI

8. **Install the AI extension.** Extensions icon → search "Codex" (OpenAI) → Install. Link to the marketplace page.
9. **Sign in with your BYU-I account.** Point to the Codex setup deck for the workspace screens. *Check: the Codex sidebar shows a chat box.*
10. **Open the AI sidebar.** Command palette → "Codex: Open Codex Sidebar." Pin it to the right side.

### Part 4: Give it a toolbox

11. **Why the AI needs tools.** Without tools it can only talk about your files. With them it can build, run, and check. Show the tool table as a one-slide map.
12. **Open the terminal and install the package manager.** Terminal → New Terminal. Mac: Homebrew one-liner. Windows: confirm `winget` works. *Check: version prints.*
13. **Git, uv, Quarto.** One slide, Mac and Windows commands side by side. *Check: three version numbers.* Note that uv will manage Python from here on.
14. **Playwright and Node.** `uvx playwright install chromium`, then Node LTS. Say what each is for in one line. *Check: two more version numbers.*
15. **Create a GitHub account.** For people without one. Go to github.com/signup, choose an email you will keep (personal is fine; a BYU-I address works but may change), pick a professional username, verify the email, and turn on two-factor authentication. Free plan is enough. *Check: you can sign in at github.com and see an empty profile.* Reassure: nothing you make is public unless you choose that.
16. **Connect GitHub to your computer.** Install `gh` (Mac `brew install gh`; Windows `winget install GitHub.cli`), then run `gh auth login` and follow the browser prompts (GitHub.com, HTTPS, log in with browser). Have the AI set the Git name and email. *Check: `gh auth status` says "Logged in."*
17. **Let the AI check its own toolbox.** Prompt: "Run the version command for git, uv, quarto, gh, node, and playwright, check that I am logged in to GitHub, and tell me what is missing." The AI reports, and can fix anything missing (human approves each command).

### Part 5: Use it for real

18. **Build something and see it.** Prompt: "Make a one-slide Quarto deck about [a topic from my course], render it, and use Playwright to screenshot it." The audience sees the file, the render, and the screenshot.
19. **Let it change a file.** Prompt: "Make the title bigger and use a navy background." Show the proposed edit, then Accept / Reject, and a new screenshot.
20. **You stay in charge.** Read what it changed. Use Git to see the diff and undo it. What to check before trusting a result. (Ties to the Brooks "volition" framing from the workshop deck.)
21. **Where to go next.** Try it on a real task (syllabus, quiz bank, data file); optionally save the project to GitHub (`gh repo create`); link to the Codex setup deck and the workshop deck; common problems.

## Backup slides

- Mac install commands, step by step.
- Windows install commands, step by step (PowerShell vs. Command Prompt, restart the terminal after installing).
- GitHub account troubleshooting: verification email missing, username taken, lost two-factor device (recovery codes), `gh auth login` browser step stuck.
- Troubleshooting: command not found (restart the terminal / PATH), sign-in loop, firewall blocks.
- "What is the terminal?" in one slide.
- **R with rig.** Install rig (Mac: `brew install rig`; Windows: `winget install posit.rig`), then `rig add release` to install the current R and `R --version` to check. Explain why: rig does for R what uv does for Python, so there is no installer-hunting and versions are easy to switch. Quarto can then run R code chunks. Optional follow-up: Positron or the VS Code R extension.
- Optional installs: TinyTeX for PDF output (`quarto install tinytex`).

## Appendix A: Using Claude instead of Codex

Same deck path, different assistant. Verify every command on a clean machine before presenting.

- **A1. Claude in VS Code.** What is different from Codex: separate account and sign-in, same sidebar-plus-tools idea.
- **A2. Install the Claude Code extension.** Extensions icon → search "Claude Code" (Anthropic) → Install. *Check: the Claude panel opens.*
- **A3. Sign in.** Sign in with a personal Claude subscription (Pro or Max) and what happens at first launch. No API key setup.
- **A4. Claude Code in the terminal (optional).** Install command for Mac and Windows, then `claude --version`.
- **A5. Same prompts, new assistant.** Re-run the toolbox check (slide 17) and the Quarto + Playwright demo (slide 18) with Claude.
- **A6. Codex or Claude?** One-line comparison: BYU-I access and cost, where each runs, approval prompts.

## Appendix B: Tool profiles (one slide per tool)

One slide for each tool attendees install, so the main slides stay short. Each tool name on a main slide links to its profile, and each profile has a "Back" link to the slide it came from.

**Profile slide template** (same layout every time, so they are quick to scan):

- **Title:** the tool name and a plain-words tagline, e.g. *Git: the undo button for your files*
- **What it is:** two sentences, no jargon.
- **What the AI uses it for:** one concrete example in the AI's words, e.g. "Show me what changed since yesterday."
- **Try it:** one command or prompt and what you should see.
- **Learn more:** link to the product website.
- **← Back to the install slide** (link).

**Profiles and where they link**

| Profile id | Tool | Linked from main slide | Tagline |
|------------|------|------------------------|---------|
| `#tool-vscode` | [VS Code](https://code.visualstudio.com) | 4 (`#download-vscode`) | The editor where everything happens |
| `#tool-codex` | [Codex extension](https://marketplace.visualstudio.com/items?itemName=OpenAI.chatgpt) | 8 (`#install-ai-extension`) | The AI helper in your sidebar |
| `#tool-package-manager` | [Homebrew](https://brew.sh) / [winget](https://learn.microsoft.com/windows/package-manager/winget/) | 12 (`#install-package-manager`) | An app store for the terminal |
| `#tool-git` | [Git](https://git-scm.com) | 13 (`#install-git-uv-quarto`) | The undo button for your files |
| `#tool-uv` | [uv](https://docs.astral.sh/uv/) | 13 (`#install-git-uv-quarto`) | Python without the setup headaches |
| `#tool-quarto` | [Quarto](https://quarto.org) | 13 (`#install-git-uv-quarto`) | Text in, slides and documents out |
| `#tool-playwright` | [Playwright](https://playwright.dev) | 14 (`#install-playwright-node`) | Lets the AI see a web page |
| `#tool-node` | [Node.js](https://nodejs.org) | 14 (`#install-playwright-node`) | The engine behind many AI tools |
| `#tool-github` | [GitHub](https://github.com) account | 15 (`#create-github-account`) | Where your work can live online |
| `#tool-gh` | [GitHub CLI](https://cli.github.com) | 16 (`#connect-github`) | GitHub from the terminal, no passwords |
| `#tool-rig` | [rig](https://github.com/r-lib/rig) | Backup: R with rig (`#backup-r-rig`) | uv, but for R |

Profile slides are ordered as in the table. Slides that cover three tools (13) link to each profile separately, and each profile returns to the same slide.

**How the links work in Quarto/RevealJS** (for the build step)

- Give every linked slide a stable id in its heading: `## Git, uv, Quarto {#install-git-uv-quarto}`.
- Main slide to profile: `[What is Git?](#/tool-git)`. RevealJS slide links use `#/slide-id`.
- Profile back to the main slide: `[← Back to install](#/install-git-uv-quarto)`.
- Profile slides sit after the Claude appendix and are reached by link (or the overview, `O`), not by paging through the deck.
- Test every link in the rendered HTML, since a typo in an id fails silently.

## Optional extras (cut first)

- Activity: each person builds a small teaching tool (reuse the Codex deck activity).
- Using a BYU-I email on GitHub: pros and cons, and how to add a second email later.
- Slide on approval prompts: what "allow this command" means and when to say no.

## Assets needed

- Screenshots, Mac and Windows: VS Code download page, installer, welcome screen, Open Folder dialog, Extensions search, Codex sidebar, terminal with the version checks.
- A tested command sheet for each OS, run on a clean machine or fresh user account before the workshop.
- The demo Quarto deck and its Playwright screenshot.
- `lead-slide.png` once the deck is rendered.

## Open questions

Decided:

1. Teach Codex; Claude goes in an appendix.
2. No admin-rights path.
3. Demo build: assumed a teaching task (a one-slide Quarto deck on a topic the attendee picks), not the generic "My First AI Deck". Confirm.
4. Standalone deck.
5. R is a backup slide, installed with rig.

6. Claude appendix assumes attendees use a personal Claude subscription (no API key path).
7. The Codex deck does not link to this one; the two decks stay independent.

Nothing is open. Next step: draft the Quarto deck from this outline.
