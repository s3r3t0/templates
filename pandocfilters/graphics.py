#!/usr/bin/env python
"""A pandoc filter that has the LaTeX writer use custom graphics environment.

Usage:
    pandoc --filter ./graphics.py -o myfile.tex myfile.md
"""

import panflute as pf


def unpack_attributes(attrs: dict[str, str]) -> str:
    result = []
    for key, value in attrs.items():
        if key in ("width", "height") and "%" in value:
            value = str(int(value.rstrip("%")) / 100.0) + r"\textwidth"
        result.append(f"{key}={value}")
    return ", ".join(result)


def graphics(elem: pf.Element, doc: pf.Doc) -> list[pf.RawInline] | None:
    if not isinstance(elem, pf.Image) or doc.format != "latex":
        return None

    url = elem.url
    attrs = elem.attributes

    return [
        pf.RawInline(
            text=r"\begin{figure}[H]"
            + r"\centering"
            + r"\includegraphics["
            + unpack_attributes(attrs)
            + "]{"
            + url
            + r"}\end{figure}",
            format="latex",
        )
    ]


def main():
    """cli entry point"""
    pf.run_filter(graphics)


if __name__ == "__main__":
    main()
