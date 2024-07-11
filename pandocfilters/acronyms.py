#!/usr/bin/env python
''' A pandoc filter for translating markdown acronym tags
    into latex glossaries tags in short form

Usage:
    pandoc --filter ./acronyms.py -o myfile.tex myfile.md
'''

import re
from pandocfilters import toJSONFilter, RawInline

tags = {
    ':': 'ac',
    ':<': 'acs',
    ':>': 'acl',
    ':!': 'acf',
    '+:': 'acp',
    '+:<': 'acsp',
    '+:>': 'aclp',
    '+:!': 'acfp',
    '^:': 'Ac',
    '^:<': 'Acs',
    '^:>': 'Acl',
    '^:!': 'Acf',
    '+^:': 'Acp',
    '+^:<': 'Acsp',
    '+^:>': 'Aclp',
    '+^:!': 'Acfp'
}


regex = re.compile(r'''# regex for acronym tag in format [!+^acronym!]
    (?P<opening>\[!)      # Opening part of the acronym tag
    (?P<prefix>\+?\^?)    # Optional plural and capitalized prefixes
    (?P<tag>[a-zA-Z]+)    # Acronym id
    (?P<extension>[<>!]?) # Optional suffix for choice of the display form
    (?P<closing>\])       # Closing part of the acronym tag ''',
                   re.VERBOSE)


def acronyms(key, value, format, meta):
    ''' Translate the acronym tags.

    Args:
        key     type of pandoc object
        value   contents of pandoc object
        format  target output format
        meta    document metadata
    '''

    if format != 'latex' or key != 'Str':
        return

    match = re.search(regex, value)

    if match:
        return [RawInline(format, value[:match.start()]),
                RawInline(format, '\\'
                          + tags[match.group('prefix')
                                 + ':'
                                 + match.group('extension')]
                          + '{'
                          + match.group('tag') + '}'),
                RawInline(format, value[match.end():])]


def main():
    """cli entry point"""
    toJSONFilter(acronyms)


if __name__ == '__main__':
    main()
