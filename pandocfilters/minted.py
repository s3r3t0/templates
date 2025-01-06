#!/usr/bin/env python
''' A pandoc LaTeX filter for code highlighting with pygments.

Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
'''

from pandocfilters import toJSONFilter, RawBlock, RawInline
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
    if 'source' in attributes.keys():
        # TODO: load code from file
        text = r'\verb|' + str(attributes) + r'|'
        Element = RawInline
    elif key == 'CodeBlock':
        Element = RawBlock
        text = highlight_code(text, language)
    elif key == 'Code':
        text = r'\verb|' + text + r'|'
        Element = RawInline
    else:
        return

    return [Element(format, text)]


def main():
    """cli entry point"""
    toJSONFilter(verbatim)


if __name__ == '__main__':
    main()
