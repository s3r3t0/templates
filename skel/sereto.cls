\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{sereto}[2024/06/01 SeReTo LaTeX class]

\LoadClass[captions=tableheading]{scrbook}

\RequirePackage{amsmath,amssymb}
\RequirePackage{setspace}
\RequirePackage{unicode-math}
\RequirePackage{lmodern}
% minted for code highlighting
\RequirePackage[outputdir=.build_artifacts]{minted}
% colors
\RequirePackage{xcolor}
% page layout
\RequirePackage[margin=2.5cm,includehead=true,includefoot=true,centering]{geometry}
% extending options for including pictures
\RequirePackage{graphicx}
% floating figures and tables
\RequirePackage{float}
% tables
\RequirePackage{longtable,booktabs,array,colortbl}
% letterspacing, underlining, overstriking, highlighting
\RequirePackage[normalem]{ulem}
% advanced quotation
\RequirePackage[style=american]{csquotes}
% cross-referencing and urls
\RequirePackage{bookmark}
% url breaking
\RequirePackage{xurl}
% captions
\RequirePackage[font={stretch=1.2},textfont={color=caption-color},position=top,skip=4mm,labelfont=bf,singlelinecheck=false,justification=raggedright]{caption}
% font
\RequirePackage[default]{sourcesanspro}
\RequirePackage{sourcecodepro}
% color boxes
\RequirePackage{tcolorbox}
% header and footer
\RequirePackage[headsepline,footsepline]{scrlayer-scrpage}

% set spacing
\setstretch{1.2}
\KOMAoptions{parskip=half}

% set fonts
\defaultfontfeatures{Scale=MatchLowercase}
\defaultfontfeatures[\rmfamily]{Ligatures=TeX,Scale=1}

% set colors
\definecolor{default-linkcolor}{HTML}{A50000}
\definecolor{default-filecolor}{HTML}{A50000}
\definecolor{default-citecolor}{HTML}{4077C0}
\definecolor{default-urlcolor}{HTML}{4077C0}
\definecolor{caption-color}{HTML}{777777}
\definecolor{heading-color}{HTML}{282828}
\definecolor{table-rule-color}{HTML}{999999}
\definecolor{code-bg-color}{HTML}{F7F7F7}
\definecolor{code-border-color}{HTML}{B3B2B3}
\definecolor{code-numbers-color}{HTML}{B3B2B3}

% minted settings
\setminted{
    autogobble=true,
    breaklines=true,
    breakanywhere=true,
    linenos=true,
    numbers=left,
    showspaces=false,
    showtabs=false,
}
%\setmintedinline{fontsize=\normalsize}
\newcommand{\mintedpath}{./outputs/}
\renewcommand{\theFancyVerbLine}{\color{code-numbers-color}\arabic{FancyVerbLine}}
\newtcolorbox{mintedbox}{
    colback=code-bg-color,
    colframe=code-border-color,
    boxrule=0.5pt,
    before skip=1em,
    after skip=1em,
    left=2.7em,
    right=0.4em,
}
\BeforeBeginEnvironment{minted}{\begin{mintedbox}}
\AfterEndEnvironment{minted}{\end{mintedbox}}
\renewcommand{\inputminted}[3][]{%
    \begin{mintedbox}
        \begingroup
        \minted@configlang{#2}%
        \setkeys{minted@opt@cmd}{#1}%
        \minted@fvset
        \minted@pygmentize[#3]{#2}%
        \endgroup
    \end{mintedbox}}

% graphics settings
\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
\def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}
\graphicspath{{./pictures/}}
\setkeys{Gin}{width=\textwidth,height=\maxheight,keepaspectratio}
\floatplacement{figure}{H}

% list settings
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}

% heading settings
\setcounter{secnumdepth}{2}
\ifx\paragraph\undefined\else
    \let\oldparagraph\paragraph
    \renewcommand{\paragraph}[1]{\oldparagraph{#1}\mbox{}}
\fi
\ifx\subparagraph\undefined\else
    \let\oldsubparagraph\subparagraph
    \renewcommand{\subparagraph}[1]{\oldsubparagraph{#1}\mbox{}}
\fi
\addtokomafont{section}{\color{heading-color}}
\addtokomafont{chapter}{\color{heading-color}}
\deftripstyle{chapterStyle}{}{}{}{}{\pagemark}{}
\renewcommand*{\chapterpagestyle}{chapterStyle}

% header and footer settings
\newpairofpagestyles{seretoStyle}{
    \clearpairofpagestyles
    \ihead*{\@title}
    \chead*{}
    \ohead*{\@date}
    \ifoot*{\@author}
    \cfoot*{}
    \ofoot*{\thepage}
    \addtokomafont{pageheadfoot}{\upshape}
}
\pagestyle{seretoStyle}

% hyperref settings
\hypersetup{
    pdftitle={},
    pdfauthor={},
    colorlinks=true,
    linkcolor=default-linkcolor,
    filecolor=default-filecolor,
    citecolor=default-citecolor,
    urlcolor=default-urlcolor,
    breaklinks=true,
    pdfcreator={}%
}

% caption settings
\setcapindent{0em}

% table settings
\arrayrulecolor{table-rule-color}
\setlength\heavyrulewidth{0.3ex}
\renewcommand{\arraystretch}{1.3}

% paragraph settings
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 2pt minus 1pt}
\setlength{\emergencystretch}{3em}

% Front matter

\renewcommand{\maketitle}{
    \begin{titlepage}
        \newgeometry{left=6cm}
        \begin{flushleft}
            \noindent
            \\[-1em]
            \color[HTML]{5F5F5F}
            \makebox[0pt][l]{\textcolor[HTML]{435488}{\rule{1.3\textwidth}{4pt}}}
            \par
            \noindent
            \setstretch{1.4}
            \vfill
            \noindent {\huge \textbf{\textsf{\@title}}}
            \vskip 1em
            {\Large \textsf{\@subtitle}}
            \vskip 2em
            \noindent {\Large \textsf{\@author}}
            \vfill
            \textsf{\@date}
        \end{flushleft}
    \end{titlepage}
    \restoregeometry
}

\newcommand{\makefront}{
    \pagenumbering{gooble}
    \maketitle
    \pagenumbering{roman}
    \tableofcontents
    \clearpage
    \pagenumbering{arabic}
}

