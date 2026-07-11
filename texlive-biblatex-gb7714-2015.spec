%global tl_name biblatex-gb7714-2015
%global tl_revision 79337

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1x
Release:	%{tl_revision}.1
Summary:	A BibLaTeX implementation of the GB/T 7714 series bibliography styles for Chi...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-contrib/biblatex-gb7714-2015
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gb7714-2015.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gb7714-2015.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the implementation of bibliography styles for the
GB/T 7714 series standards, such as GB/T 7714-1987, GB/T 7714-2005, GB/T
7714-2015, GB/T 7714-2025. The package also provides several liberal
arts bibliography styles, such as chinese-erj, chinese-css, chinese-jmw,
and so on. These styles can be used simply by loading BibLaTeX with the
appropriate option.

