%global tl_name asaetr
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0a
Release:	%{tl_revision}.1
Summary:	Transactions of the ASAE
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/asaetr
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asaetr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/asaetr.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class and BibTeX style for submissions to the Transactions of the
American Society of Agricultural Engineers. Also included is the
Metafont source of a slanted Computer Modern Caps and Small Caps font.

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
%dir %{_datadir}/texmf-dist/bibtex
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/bibtex/bst
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/bibtex/bst/asaetr
%dir %{_datadir}/texmf-dist/doc/latex/asaetr
%dir %{_datadir}/texmf-dist/tex/latex/asaetr
%{_datadir}/texmf-dist/bibtex/bst/asaetr/asaetr.bst
%doc %{_datadir}/texmf-dist/doc/latex/asaetr/MANIFEST
%doc %{_datadir}/texmf-dist/doc/latex/asaetr/asaetr.bib
%doc %{_datadir}/texmf-dist/doc/latex/asaetr/asaetr.pdf
%doc %{_datadir}/texmf-dist/doc/latex/asaetr/asaetr.tex
%doc %{_datadir}/texmf-dist/doc/latex/asaetr/cmcscsl10.mf
%{_datadir}/texmf-dist/tex/latex/asaetr/asaesub.sty
%{_datadir}/texmf-dist/tex/latex/asaetr/asaetr.cls
%{_datadir}/texmf-dist/tex/latex/asaetr/asaetr.sty
