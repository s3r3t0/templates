#!/usr/bin/env python
"""A pandoc filter for translating markdown acronym tags
    into latex glossaries tags in short form

Usage:
    pandoc --filter ./acronyms.py -o myfile.tex myfile.md
"""

import re

import panflute as pf

tags = {
    ":": "ac",
    ":<": "acs",
    ":>": "acl",
    ":!": "acf",
    "+:": "acp",
    "+:<": "acsp",
    "+:>": "aclp",
    "+:!": "acfp",
    "^:": "Ac",
    "^:<": "Acs",
    "^:>": "Acl",
    "^:!": "Acf",
    "+^:": "Acp",
    "+^:<": "Acsp",
    "+^:>": "Aclp",
    "+^:!": "Acfp",
}


regex = re.compile(
    r"""# regex for acronym tag in format [!+^acronym!]
    (?P<opening>\[!)      # Opening part of the acronym tag
    (?P<prefix>\+?\^?)    # Optional plural and capitalized prefixes
    (?P<tag>[\w-]+)       # Acronym id
    (?P<extension>[<>!]?) # Optional suffix for choice of the display form
    (?P<closing>\])       # Closing part of the acronym tag """,
    re.VERBOSE,
)


def acronyms(elem: pf.Element, doc: pf.Doc) -> list[pf.RawInline] | None:
    """Translate the acronym tags.

    Args:
        elem    pandoc element
        doc     pandoc document
    """

    if not isinstance(elem, pf.Str) or doc.format != "latex":
        return None

    match = re.search(regex, elem.text)

    if not match:
        return None

    prefix = elem.text[: match.start()]
    suffix = elem.text[match.end() :]

    tag = "\\" + tags[match.group("prefix") + ":" + match.group("extension")] + "{" + match.group("tag") + "}"
    return [pf.RawInline(text=t, format=doc.format) for t in [prefix, tag, suffix] if t]


def main() -> None:
    """cli entry point"""
    pf.run_filter(acronyms)


if __name__ == "__main__":
    main()
