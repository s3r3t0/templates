# Security Reporting Tool Templates

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/s3r3t0/sereto/main/docs/assets/logo/sereto_block_white.svg">
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/s3r3t0/sereto/main/docs/assets/logo/sereto_block_black.svg">
  <img src="https://raw.githubusercontent.com/s3r3t0/sereto/main/docs/assets/logo/sereto_block_black.svg" alt="SeReTo logo" align="right" height="150"/>
</picture>

[![GitHub release](https://img.shields.io/github/v/release/s3r3t0/templates)][release]
[![GitHub release date](https://img.shields.io/github/release-date/s3r3t0/templates)][release]
[![GitHub last commit](https://img.shields.io/github/last-commit/s3r3t0/templates)](https://github.com/s3r3t0/templates/commit/main)

[![Documentation](https://img.shields.io/badge/documentation-SeReTo-blue)](https://sereto.s4n.cz/)
[![GitHub License](https://img.shields.io/github/license/s3r3t0/templates)][license]
![GitHub language count](https://img.shields.io/github/languages/count/s3r3t0/templates)
![GitHub top language](https://img.shields.io/github/languages/top/s3r3t0/templates)

[![Debian package](https://img.shields.io/debian/v/pandoc?label=pandoc)][pandoc-manual]
[![Fedora package](https://img.shields.io/fedora/v/pandoc?label=pandoc)][pandoc-manual]
[![jinja2 version](https://img.shields.io/badge/jinja2-v3.1.0-blue)](https://jinja.palletsprojects.com/en/stable/)

A basic template structure for documents created with the [Security Reporting Tool (SeReTo)][SeReTo].

The style is inspired by the [Eisvogel] pandoc LaTeX template.

## Table of Contents

- [Security Reporting Tool Templates](#security-reporting-tool-templates)
  - [Table of Contents](#table-of-contents)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installing](#installing)
  - [Versioning](#versioning)
  - [License](#license)
  - [FAQ](#faq)
    - [Does it work with version of SeReTo I have installed?](#does-it-work-with-version-of-sereto-i-have-installed)
  - [Acknowledgements](#acknowledgements)

## Getting Started

These instructions will get you a copy of the project ready for use on your local machine.
You will be ready to create documents with the [SeReTo] and improve your own templates.

### Prerequisites

Please, follow [SeReTo installation instructions][install] before you start using the templates.

### Installing

You can use our repository as a [template] while creating your own template project.

Or you can download a source code archive and unpack it.

```bash
curl -L https://api.github.com/repos/s3r3t0/templates/tarball/main -o /tmp/sereto_templates
tar -xzvf /tmp/sereto_templates "$HOME/sereto_templates"
```

You will be prompted to configure the template path when you run the [SeReTo] for the first time.

## Versioning

We use [Semantic Versioning][semver] for versioning. For the versions available, see the [tags on this repository][tags] or the full [Changelog].

We keep the major and minor version of the template in sync with [SeReTo].
The latest version of the template is tested with the latest version of SeReTo.

## License

This project is licensed under the [BSD 3-Clause License][license] - see the [LICENSE.md][license] file for details.

## FAQ

### Does it work with version of SeReTo I have installed?

The latest version of the template is tested with the latest version of SeReTo.
The major and minor versions of the template and SeReTo should match.
Patch versions are reserved for changes related to the template only.

## Acknowledgements

The style is inspired by the [Eisvogel] pandoc LaTeX template.

> Created with support of [NN Management Services, s.r.o.][nn]

[SeReTo]: https://github.com/s3r3t0/sereto
[Eisvogel]: https://github.com/Wandmalfarbe/pandoc-latex-template
[install]: https://sereto.s4n.cz/getting_started/installation/
[template]: https://github.com/new?template_name=templates&template_owner=s3r3t0
[semver]: https://semver.org
[tags]: https://github.com/s3r3t0/templates/tags
[license]: https://github.com/s3r3t0/templates/blob/main/LICENSE.md
[Changelog]: https://github.com/s3r3t0/templates/blob/main/CHANGELOG.md
[nn]: https://www.nn.cz/kariera/en/nn-digital-hub/
[release]: https://github.com/s3r3t0/templates/releases/latest
[pandoc-manual]: https://pandoc.org/MANUAL.html
