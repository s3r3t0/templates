#!/usr/bin/env python
"""A pandoc LaTeX filter for code highlighting with pygments.

Usage:
    pandoc --filter ./verbatim.py -o myfile.tex myfile.md
"""

import panflute as pf
from click import echo
from pygments import highlight
from pygments.formatters import LatexFormatter
from pygments.lexers import get_lexer_by_name


def highlight_code(code: str, language: str) -> str:
    """Highlight code with pygments.

    Args:
        code      source code to highlight
        language  programming language of the source code
    """
    try:
        lexer = get_lexer_by_name(language, stripall=True)
    except Exception:
        echo(f"Pygments: lexer not found for {language}.", err=True)
        lexer = get_lexer_by_name("text", stripall=True)
    formatter = LatexFormatter()
    return highlight(code, lexer, formatter)


def verbatim(elem: pf.Element, doc: pf.Doc) -> list[pf.RawBlock] | list[pf.RawInline] | None:
    """Process verbatim objects.

    Args:
        elem    pandoc element
        doc     pandoc document

    Returns:
        list[pf.RawBlock]: A single highlighted LaTeX raw block when `elem` is a
            ``pf.CodeBlock`` and output format is LaTeX.
        list[pf.RawInline]: A single LaTeX raw inline verbatim element when `elem`
            is ``pf.Code`` and output format is LaTeX.
        None: If output format is not LaTeX or `elem` is not a supported code
            element.
    """
    if doc.format != "latex":
        return None

    if isinstance(elem, pf.CodeBlock):
        language = elem.classes[0] if elem.classes else "text"
        text = highlight_code(elem.text, language)
        return [pf.RawBlock(text=text, format="latex")]
    elif isinstance(elem, pf.Code):
        delimiters = ["|", "/", "!", "+", ";", ":", "~", "#", "@", "%", "^", "&", "*", "-", "_", "="]
        delimiter = next((d for d in delimiters if d not in elem.text), None)
        if delimiter is None:
            # Fallback: keep command syntactically valid even for pathological input.
            delimiter = "|"
            inline_text = elem.text.replace("|", r"\|")
        else:
            inline_text = elem.text
        text = rf"\Verb{delimiter}{inline_text}{delimiter}"
        return [pf.RawInline(text=text, format="latex")]

    return None


def main():
    """cli entry point"""
    pf.run_filter(verbatim)


if __name__ == "__main__":
    main()
