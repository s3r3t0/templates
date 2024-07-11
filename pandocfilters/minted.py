#!/usr/bin/env python
''' A pandoc filter that has the LaTeX writer use minted for typesetting code.

Usage:
    pandoc --filter ./minted.py -o myfile.tex myfile.md
'''

from string import Template
from pandocfilters import toJSONFilter, RawBlock, RawInline


def minted(key, value, format, meta):
    ''' Use minted for code in LaTeX.

    Args:
        key     type of pandoc object
        value   contents of pandoc object
        format  target output format
        meta    document metadata
    '''
    if format != 'latex':
        return

    # Determine what kind of code object this is.
    if key == 'CodeBlock':
        template = Template(
            '\\begin{minted}[$attr]{$l}\n$code\n\\end{minted}'
        )
        Element = RawBlock
    elif key == 'Code':
        template = Template('\\mintinline[$attr]{$l}|$code|')
        Element = RawInline
    else:
        return

    [[id, cls, kv], text] = value

    # check if source is in file
    attributes = []
    for k, v in kv:
        if k == 'source':
            template = Template('\\inputminted[$attr]{$l}{\\mintedpath $code}')
            Element = RawInline
            text = v
        else:
            attributes.append(k + '={' + v + '}')

    language = cls[0] if len(cls) else 'text'

    return [Element(format, template.substitute(attr=', '.join(attributes),
                    l=language,
                    code=text))]


def main():
    """cli entry point"""
    toJSONFilter(minted)


if __name__ == '__main__':
    main()
