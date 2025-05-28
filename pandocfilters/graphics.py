#!/usr/bin/env python
''' A pandoc filter that has the LaTeX writer use custom graphics environment.

Usage:
    pandoc --filter ./graphics.py -o myfile.tex myfile.md
'''

from pandocfilters import toJSONFilter, RawInline


def unpack_attributes(attributes):
    ''' Unpack the image attributes.

    Args:
        attributes       pandoc Attr object
    '''
    id, cls, kv = attributes
    result = []

    for key, value in kv:
        if key in ['width', 'height']:
            if value.find('%') >= 0:
                value = str(int(value.rstrip('%'))/100.0) + r'\textwidth'
        result.append('='.join([key, value]))

    return ', '.join(result)


def graphics(key, value, format, meta):
    ''' Use custom figure environment in LaTeX.

    Args:
        key     type of pandoc object
        value   contents of pandoc object
        format  target output format
        meta    document metadata
    '''
    if format != 'latex' or key != 'Image':
        return

    [attributes, alt, [url, title]] = value

    return [RawInline(format, r'\begin{figure}[H]'
                      + r'\centering'
                      + r'\includegraphics['
                      + unpack_attributes(attributes)
                      + ']{'
                      + url
                      + '}'
                      + r'\end{figure}')
            ]


def main():
    """cli entry point"""
    toJSONFilter(graphics)


if __name__ == '__main__':
    main()
