#!/usr/bin/env python
''' A pandoc LaTeX filter for code highlighting with pygments.

Usage:
    pandoc --filter ./verbatim.py -o myfile.tex myfile.md
'''

from pandocfilters import toJSONFilter, RawBlock, RawInline
from click import echo
from pygments import highlight
from pygments.formatters import LatexFormatter
from pygments.lexers import get_lexer_by_name


def highlight_code(code, language):
    ''' Highlight code with pygments.

    Args:
        code      source code to highlight
        language  programming language of the source code
    '''
    try:
        lexer = get_lexer_by_name(language, stripall=True)
    except Exception:
        echo(f'Pygments: lexer not found for {language}.', err=True)
        lexer = get_lexer_by_name('text', stripall=True)
    formatter = LatexFormatter()
    return highlight(code, lexer, formatter)


def verbatim(key, value, format, meta):
    ''' Process verbatim objects.

    Args:
        key     type of pandoc object
        value   contents of pandoc object
        format  target output format
        meta    document metadata
    '''
    if format != 'latex':
        return

    if key not in ['CodeBlock', 'Code']:
        return

    [[id, cls, kv], text] = value

    # Process attributes
    attributes = dict(kv)

    language = cls[0] if len(cls) else 'text'

    # Determine what kind of code object this is.
    if key == 'CodeBlock':
        Element = RawBlock
        text = highlight_code(text, language)
    elif key == 'Code':
        text = r'\Verb|' + text + r'|'
        Element = RawInline

    return [Element(format, text)]


def main():
    """cli entry point"""
    toJSONFilter(verbatim)


if __name__ == '__main__':
    main()
