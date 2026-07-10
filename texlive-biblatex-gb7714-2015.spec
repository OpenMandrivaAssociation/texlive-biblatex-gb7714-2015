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
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides the implementation of bibliography styles for the
GB/T 7714 series standards, such as GB/T 7714-1987, GB/T 7714-2005, GB/T
7714-2015, GB/T 7714-2025. The package also provides several liberal
arts bibliography styles, such as chinese-erj, chinese-css, chinese-jmw,
and so on. These styles can be used simply by loading BibLaTeX with the
appropriate option.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015
%dir %{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015/README.md
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015/biblatex-gb7714-2015-preamble.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015/biblatex-gb7714-2015.pdf
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015/biblatex-gb7714-2015.tex
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015/example.bib
%doc %{_datadir}/texmf-dist/doc/latex/biblatex-gb7714-2015/gb7714texttobib.pl
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-cajhss.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-cajhss.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-cajhssay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-cajhssay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-css.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-css.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-erj.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-erj.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-jmw.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-jmw.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-molc.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/chinese-molc.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-1987.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-1987.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-1987ay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-1987ay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2005.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2005.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2005ay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2005ay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015-gbk.def
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015ay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015ay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015ms.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015ms.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015mx.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2015mx.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2025.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2025.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2025ay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2025ay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-2025v1.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-CCNU.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-CCNU.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-CCNUay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-CCNUay.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-NWAFU.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-NWAFU.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-SEU.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714-SEU.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714.cbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714ay.bbx
%{_datadir}/texmf-dist/tex/latex/biblatex-gb7714-2015/gb7714ay.cbx
