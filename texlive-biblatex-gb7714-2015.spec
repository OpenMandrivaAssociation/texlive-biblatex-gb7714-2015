Name:		texlive-biblatex-gb7714-2015
Version:	71329
Release:	1
Summary:	A BibLaTeX implementation of the GBT7714-2015 bibliography style for Chinese users
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/biblatex-gb7714-2015
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gb7714-2015.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/biblatex-gb7714-2015.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides an implementation of the GBT7714-2015
bibliography style. This implementation follows the
GBT7714-2015 standard and can be used by simply loading
BibLaTeX with the appropriate option. A demonstration database
is provided to show how to format input for the style.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/biblatex-gb7714-2015
%doc %{_texmfdistdir}/doc/latex/biblatex-gb7714-2015

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
