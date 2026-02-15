# AGENTS.md — SeReTo Project Guide

## Project Overview

- This is a **SeReTo (Security Reporting Tool) project** — a penetration test report authored in Markdown and LaTeX, rendered to PDF.
- Processed by the [SeReTo CLI](https://github.com/s3r3t0/sereto) with [XeLaTeX](https://tug.org/xetex/) and [Pandoc](https://pandoc.org/) (≥ v3.1.2).
- All content is written in **English**.

## Project Structure

| Path | Purpose | Editable? |
|------|---------|-----------|
| `layouts/` | Jinja2/LaTeX page layouts (report, target, finding_group, sow, debug) | Yes — advanced customisation only |
| `layouts/_base.tex.j2` | Base layout inherited by all others | ⚠️ Edit with caution — affects every output |
| `includes/sereto.cls` | Core LaTeX document class (page setup, fonts, colours, macros) | **Do not edit** |
| `includes/pygments.sty` | Pygments syntax-highlighting style for code blocks | **Do not edit** |
| `includes/macros.tex.j2` | Reusable Jinja2/LaTeX macros (findings table, detail boxes) | Yes |
| `includes/glossary.tex` | Acronym definitions using LaTeX `glossaries` package (`\newacronym`) | Yes — add new terms here |
| `pictures/` | Logo SVG and potential screenshots | Yes — add/replace images |
| `<target>/` | Per-target content directories (scope, approach, findings) | Yes — primary editing area |
| `<target>/findings.toml` | Declares which findings to include and their grouping | Yes |
| `<target>/scope.tex.j2` | Target scope description | Yes |
| `<target>/approach.tex.j2` | Target approach/methodology description | Yes |
| `.build/` | Auto-generated build artefacts | **Do not edit — do not commit** |
| `pdf/` | Generated PDF output | **Do not edit — do not commit** |
| `.sereto` | Project marker file | **Do not edit** |
| `.seretoignore` | Files excluded from report attachments | Yes |
| `outputs/sereto` | Branding marker | **Do not edit** |
| `attachment_exclude/` | Files to exclude from attachments | Yes |

## Content Authoring — Findings

Findings are Markdown files with Jinja2 templating (`.md.j2`), located in target directories or sourced from the template's `categories/` library.

### Finding file structure

1. **TOML frontmatter** between `+++` fences:
   ```
   +++
   name = "Human-Readable Finding Title"
   risk = "high"
   
   [[locators]]
   type = "url"
   value = "https://example.com/login"

   [variables]
   images = ["screenshot1.png", "screenshot2.png"]
   +++
   ```
2. **Extends** `_base.md` — always inherit from the category base.
3. **Override these blocks** (all are optional except `description`):

| Block | Content | Format |
|-------|---------|--------|
| `description` | **Required.** State the vulnerability factually, include evidence (screenshots, tables, code samples). | Paragraphs, tables, images |
| `likelihood` | Assess realistic exploitability. | Single paragraph or bullet list |
| `impact` | Describe consequences of exploitation. | Single paragraph or bullet list |
| `recommendation` | Actionable remediation steps. | Single paragraph or bullet list |
| `reference` | Links to authoritative sources (OWASP, MDN, vendor docs). | Bullet list of Markdown links |

### Risk levels

Use exactly one of: `critical`, `high`, `medium`, `low`, `info`, `closed`.

### Tone and wording

- Write in **third person, professional tone**.
- Use factual statements: *"The application does not set the HttpOnly flag…"*
- Avoid first person (*"I found…"*) — use *"the team discovered…"* or passive voice.
- Be specific about what was tested and what was found.

### Acronym syntax

Define acronyms in `includes/glossary.tex` using `\newacronym{label}{ABBREV}{Full Name}`, then reference them in Markdown findings:

| Syntax | Meaning | LaTeX output |
|--------|---------|-------------|
| `[!api]` | Default form | `\ac{api}` |
| `[!api<]` | Short form only | `\acs{api}` |
| `[!api>]` | Long form only | `\acl{api}` |
| `[!api!]` | Full (short + long) | `\acf{api}` |
| `[!+api]` | Plural | `\acp{api}` |
| `[!^api]` | Capitalised | `\Ac{api}` |
| `[!+^api]` | Plural + capitalised | `\Acp{api}` |

Prefixes (`+` plural, `^` capitalise) go **before** the tag. Suffixes (`<` short, `>` long, `!` full) go **after**.

### Image syntax

In Markdown findings, use standard Markdown image syntax:

```
![Alt text describing the screenshot](filename.png){width=90%}
```

- Place image files in the `pictures/` directory.
- The `\graphicspath` is set to `pictures/` by the base layout, so no path prefix is needed.
- **Do not** include the `pictures/` prefix in the Markdown `()` path.
- Supported formats: PNG, JPEG, SVG, PDF.

### Code blocks in findings

Use fenced code blocks with language annotation:

````
```http
GET / HTTP/2
Host: example.com
```
````

````
```{.py}
import os
```
````

### Tables in findings

Use standard Markdown pipe tables with alignment:

```
| Header 1 | Header 2 |
|:---------|:---------|
| cell 1   | cell 2   |
```

## LaTeX Template Syntax

Layout and target templates (`.tex.j2`) use **custom Jinja2 delimiters** to avoid conflicts with LaTeX's `{ }` braces and `%` comment character:

| Construct | Syntax | Example |
|-----------|--------|---------|
| Block tags | `((* ... *))` | `((* for t in c.targets *))` |
| Expressions | `((( ... )))` | `((( target.data.name \| tex )))` |
| Comments | `((= ... =))` | `((= Scope =))` |
| Extends | `((* extends "_base.tex.j2" *))` | |
| Include | `((* include target.uname + "/scope.tex.j2" *))` | |

> **Do not** use standard `{% %}` / `{{ }}` Jinja2 in `.tex.j2` files — they will conflict with LaTeX syntax.

### The `| tex` filter

In `.tex.j2` files, **always** pipe user-facing strings through the `| tex` Jinja2 filter to escape LaTeX special characters: `((( c.name | tex )))`. Omitting this can break compilation.

## Layout / Generated Files

- **`.build/`** — contains intermediate LaTeX/TeX files generated by SeReTo. **Never edit manually**; regenerated on every build.
- **`pdf/`** — contains final PDF output. **Never edit manually; do not commit.**
- Risk chart images (`/.build/<target>/risks.png`) are auto-generated.

## findings.toml — Finding Group Configuration

Each target directory contains a `findings.toml` that declares which findings to include:

```toml
["Finding Group Name"]
findings = ["finding_template_name"]
risk = "high"  # optional — defaults to highest risk in group
```

- Finding names reference `.md.j2` files (without extension) from the category's `findings/` directory.
- Multiple findings can be grouped: `findings = ["finding_a", "finding_b"]`.
- `risk` is optional; if omitted, it defaults to the highest risk among the group's findings.

## Conventions

- **Minimal diffs** — don't reformat files you didn't change.
- **Indentation:** 4 spaces. No tabs.
- **File naming:** `snake_case` for finding files, target directories, and skeleton files.
- Keep `glossary.tex` entries sorted alphabetically.
- Always add `{width=90%}` to finding screenshot images for consistent sizing.

## Security

- **Never commit real client data**, IP addresses, credentials, hostnames, or internal URLs.
- Use placeholder/redacted values in committed templates and examples.
- Review `.seretoignore` to ensure sensitive artefacts are excluded from attachments.
- The report PDF is marked **CONFIDENTIAL** — treat all project content accordingly.

## Communication

- **Ask before large changes** to base layouts (`_base.tex.j2`), core includes (`sereto.cls`, `macros.tex.j2`), or theme — these affect every generated output.
- **State assumptions** about which SeReTo version and template version you are targeting.
- **List what you changed** — which findings, targets, glossary entries, or layout files were modified.
- Consult the [SeReTo documentation](https://sereto.s4n.cz/) for available Jinja2 context variables and CLI commands.
