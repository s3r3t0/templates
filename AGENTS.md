# AGENTS.md — Contributor Guide for templates

## Project Overview

- **LaTeX-based report templates** for the [Security Reporting Tool (SeReTo)](https://github.com/s3r3t0/sereto), producing penetration test reports as PDF.
- **Languages/tools:** LaTeX, Jinja2 templates, Python (pandoc filters & plugins), Pandoc, Markdown.
- **Key directories:**
  - `skel/` — scaffold skeleton copied into new SeReTo projects (layouts, includes, pictures, config).
  - `categories/` — per-category templates and pre-written findings (dast, infrastructure, mobile, sast, etc.).
  - `pandocfilters/` — Python pandoc filters (acronyms → LaTeX glossaries, image handling).
  - `plugins/` — SeReTo CLI plugins (Python/Click).
- **Upstream docs:** <https://sereto.s4n.cz/>

## Setup & Dev Workflow

### Prerequisites

- **TeX Live** (or equivalent LaTeX distribution) with XeLaTeX
- **Pandoc** ≥ v3.1.2
- **Python** ≥ 3.12 (for pandoc filters and plugins)
- **uv** (recommended) or pip

### Install

```sh
# Install SeReTo CLI with template plugin dependencies
uv tool install sereto@latest --with-requirements requirements.txt
```

### Repo Map (quick reference)

| Path | Purpose |
|------|---------|
| `skel/layouts/*.tex.j2` | Jinja2/LaTeX page layouts (report, target, finding_group, sow, debug) |
| `skel/includes/sereto.cls` | Core LaTeX document class (page setup, fonts, colours, macros) |
| `skel/includes/pygments.sty` | Pygments syntax-highlighting style for code blocks |
| `skel/includes/macros.tex.j2` | Reusable Jinja2/LaTeX macros (findings table, detail boxes) |
| `skel/includes/glossary.tex` | Acronym definitions using LaTeX `glossaries` package (`\newacronym`) |
| `skel/pictures/` | Risk indicator PNGs and logo SVG |
| `categories/<cat>/target.tex.j2` | Per-category target chapter template |
| `categories/<cat>/finding_group.tex.j2` | Per-category finding-group rendering |
| `categories/<cat>/findings/*.md.j2` | Pre-written finding templates (Markdown + TOML frontmatter) |
| `categories/<cat>/skel/` | Boilerplate files copied when a target of this category is added |
| `pandocfilters/acronyms.py` | Converts `[!acronym]` syntax → LaTeX `\ac{}`/`\acp{}` commands |
| `pandocfilters/graphics.py` | Converts Markdown images → LaTeX `\includegraphics` in `figure` env |
| `pandocfilters/verbatim.py` | Highlights code blocks with Pygments and typesets inline code with `fvextra` `\Verb` |
| `plugins/test.py` | Example SeReTo CLI plugin |

## Template Syntax — Critical Rules

### Two Jinja2 dialects

| File type | Delimiters | Example |
|-----------|-----------|---------|
| **LaTeX templates** (`.tex.j2`) | `((* block *))` / `((( expr )))` / `((= comment =))` | `((( target.data.name \| tex )))` |
| **Markdown findings** (`.md.j2`) | `{% block %}` / `{{ expr }}` / `{# comment #}` | `{{ f.vars.images }}` |

> **Do not mix dialects.** LaTeX templates use `(( ))` delimiters to avoid clashing with LaTeX's `{ }` braces and `%` comment character. Markdown templates use standard Jinja2.

### The `| tex` filter

In `.tex.j2` files, **always** pipe user-facing strings through the `| tex` Jinja2 filter to escape LaTeX special characters: `((( c.name | tex )))`. Omitting this can break compilation.

### Finding file structure (`.md.j2`)

1. **TOML frontmatter** between `+++` fences: `name`, `risk`, `keywords`, `[[variables]]`.
2. **Extends** `_base.md` (each category has its own `_base.md` in `skel/findings/`).
3. **Override blocks:** `description`, `likelihood`, `impact`, `recommendation`, `reference`.
4. Risk levels (in order): `critical`, `high`, `medium`, `low`, `info`, `closed`.

### Acronym syntax (in Markdown findings)

Use `[!tag]` where `tag` matches a label in `skel/includes/glossary.tex`.

| Syntax | Meaning | LaTeX output |
|--------|---------|-------------|
| `[!api]` | default form | `\ac{api}` |
| `[!api<]` | short form | `\acs{api}` |
| `[!api>]` | long form | `\acl{api}` |
| `[!api!]` | full (short + long) | `\acf{api}` |
| `[!+api]` | plural | `\acp{api}` |
| `[!^api]` | capitalised | `\Ac{api}` |
| `[!+^api]` | plural + capitalised | `\Acp{api}` |

Prefixes (`+`, `^`) go before the tag; suffixes (`<`, `>`, `!`) go after.

### Image references

- In Markdown findings: `![alt text](filename){width=90%}` — the pandoc filter converts this to `\includegraphics`. The `\graphicspath` is set to `pictures/` by the base layout.
- In LaTeX templates: `\includegraphics[width=\textwidth]{filename}` — no path prefix needed thanks to `\graphicspath`.

## Testing & Validation

Before finishing any change:

1. **Run lint and tests:** `tox` — runs ruff lint, mypy type checking, and pytest across Python 3.12–3.14.
2. **Format code:** `tox -e format` — runs ruff (import sorting + formatting) on `pandocfilters/`, `plugins/`, and `tests/`.
3. **Individual tox environments:**
   - `tox -e lint` — ruff check on `pandocfilters/` and `plugins/`
   - `tox -e type` — mypy on `plugins/`
   - `tox -e py314` (or `py313`, `py312`) — pytest on `tests/`
4. **Render a test report** using SeReTo to verify templates compile without errors.
5. **Check LaTeX compilation:** ensure `.tex` output from Jinja2 compiles with XeLaTeX without errors.
6. **Validate TOML frontmatter** in any new/edited findings (well-formed `+++` blocks).
7. **Check glossary.tex** if you added new acronyms — use `\newacronym{label}{ABBREV}{Full Name}` format.

Always run `tox -e format` before committing Python changes. CI runs `tox -e lint` and `tox -e type` on Python 3.12.

## Coding Conventions & Architecture

### File naming

- LaTeX+Jinja2 templates: `<name>.tex.j2`
- Markdown+Jinja2 findings: `<name>.md.j2` (use `snake_case`)
- Skeleton boilerplate: plain `.tex.j2` (scope, approach, prerequisites)
- Finding names in TOML frontmatter should be title-cased human-readable strings.

### Category structure

Every category under `categories/` should contain:
- `target.tex.j2` — main target chapter (imports macros, includes scope/approach/findings)
- `finding_group.tex.j2` — finding-group detail rendering
- `findings/` — reusable finding templates
- `skel/` — skeleton files: `approach.tex.j2`, `scope.tex.j2`, `findings.toml`, `findings/_base.md`

Exception: `categories/generic/` only has `findings/` (no target/skel — used for cross-category findings).

### Patterns

- **Do** use `((* extends "_base.tex.j2" *))` for layout inheritance in LaTeX templates.
- **Do** use `{% extends "_base.md" %}` for finding inheritance in Markdown.
- **Do** use the `macros.tex.j2` helpers (`findings_table`, `finding_details`) rather than duplicating table/box markup.
- **Do** add new acronyms to `skel/includes/glossary.tex` using `\newacronym`.
- **Do** use `| tex` filter on all user-supplied text in `.tex.j2` files.
- **Don't** hardcode team/company names — use Jinja2 context variables (`team`, `company`, `c.*`).
- **Don't** put raw LaTeX in `.md.j2` files — the pandoc pipeline handles conversion.

### Writing conventions for findings

- Write in third person, professional tone: *"The application could further restrict…"*, *"During the engagement, the team discovered…"*
- `description` block: state the issue factually, include evidence (screenshots, tables).
- `likelihood` block: assess realistic exploitability. Single paragraph or bullet list.
- `impact` block: describe consequences of exploitation. Single paragraph or bullet list.
- `recommendation` block: provide actionable remediation steps. Single paragraph or bullet list.
- `reference` block: link to authoritative sources (OWASP, MDN, vendor docs).

## Change Hygiene

- **Minimal diffs** — don't reformat files you didn't change.
- **Update `CHANGELOG.md`** under `[Unreleased]` for any user-visible change.
- **Update `glossary.tex`** if you introduce new acronyms.
- **Don't add Python dependencies** to `requirements.txt` without discussion.
- **Versioning** follows [SemVer](https://semver.org/) and tracks SeReTo's major.minor version.

## Security / Secrets

- **Never commit real client data**, IP addresses, credentials, or engagement details.
- Finding templates must use placeholder/example data only.
- `skel/.seretoignore` controls what is excluded from report attachments — review it if you add new file types.
- The `skel/outputs/sereto` file is a branding marker, not executable.

## Communication / Task Handling

- **Ask before large refactors** — especially changes to `_base.tex.j2`, `sereto.cls`, or `macros.tex.j2` which affect all outputs.
- **State assumptions** about SeReTo version compatibility.
- **List what you changed** — template files, glossary entries, new findings, etc.
- If unsure about Jinja2 context variables available at render time, consult the [SeReTo documentation](https://sereto.s4n.cz/).