\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{sereto}[2025/05/26 SeReTo LaTeX class]

\LoadClass[captions=tableheading]{scrbook}

\RequirePackage{amsmath,amssymb}
\RequirePackage{setspace}
\RequirePackage{unicode-math}
\RequirePackage{lmodern}
% fancy code highlighting
\RequirePackage{fvextra}
% colors
\RequirePackage{xcolor}
% page layout
\RequirePackage[margin=2.5cm,includehead=true,includefoot=true,centering]{geometry}
% box positioning
\RequirePackage[export]{adjustbox}
% extending options for including pictures
\RequirePackage{graphicx}
% floating figures and tables
\RequirePackage{float}
% tables
\RequirePackage{longtable,booktabs,array,colortbl}
% letterspacing, underlining, overstriking, highlighting
\RequirePackage{soul}           % (Pandoc post 3.0.0)
\RequirePackage[normalem]{ulem} % (Pandoc pre 3.0.0)
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
\RequirePackage[many]{tcolorbox}
% header and footer
\RequirePackage[headsepline,footsepline]{scrlayer-scrpage}
% lists
\RequirePackage{enumitem}
% glossaries
\RequirePackage[
  acronym,
  nomain,
  shortcuts,
  nogroupskip,
  numberedsection=nolabel
]{glossaries}

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

% colorbox settings
\tcbset{breakable}

% verbatim settings
\fvset{
  breaklines=true,
  breakanywhere=true,
  linenos=true,
  numbers=left,
  showspaces=false,
  showtabs=false,
}
\renewcommand{\theFancyVerbLine}{\color{code-numbers-color}\arabic{FancyVerbLine}}
\newtcolorbox{vrbbox}{
  colback=code-bg-color,
  colframe=code-border-color,
  boxrule=0.5pt,
  before skip=1em,
  after skip=1em,
  left=2.7em,
  right=0.4em,
  breakable,
}
\BeforeBeginEnvironment{Verbatim}{\begin{vrbbox}}
\AfterEndEnvironment{Verbatim}{\end{vrbbox}}

% graphics settings
\def\maxwidth{\ifdim\Gin@nat@width>\linewidth\linewidth\else\Gin@nat@width\fi}
\def\maxheight{\ifdim\Gin@nat@height>\textheight\textheight\else\Gin@nat@height\fi}
\setkeys{Gin}{width=\textwidth,height=\maxheight,keepaspectratio}
\floatplacement{figure}{H}

% list settings
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\setlist[1]{beginpenalty=1000,
            midpenalty=10}

% heading settings
\newcommand{\tocdepth}{2}
\setcounter{secnumdepth}{\tocdepth}
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
  \ohead*{\includegraphics[height=6mm, valign=B]{logo_line}}
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

% prepare acronyms
\setglossarystyle{alttree}
\setacronymstyle{long-short}
\makenoidxglossaries

% version info
\newcommand{\@versioninfo}{\relax}
\newcommand{\versioninfo}[1]{\renewcommand{\@versioninfo}{%
  \chapter*{Version Information}
  #1%
}}

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
      \noindent
      \includegraphics[width=30mm, left]{logo}
      \textsf{\@date}
    \end{flushleft}
  \end{titlepage}
  \restoregeometry
}

\newcommand{\makefront}{
  \pagenumbering{gooble}
  \maketitle
  \pagenumbering{roman}
  \@versioninfo
  \tableofcontents
  \clearpage
  \pagenumbering{arabic}
}
