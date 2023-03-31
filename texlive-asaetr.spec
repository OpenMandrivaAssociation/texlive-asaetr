Name:		texlive-asaetr
Version:	15878
Release:	2
Summary:	Transactions of the ASAE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asaetr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asaetr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asaetr.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A class and BibTeX style for submissions to the Transactions of
the American Society of Agricultural Engineers. Also included
is the MetaFont source of a slanted Computer Modern Caps and
Small Caps font.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/bibtex/bst/asaetr/asaetr.bst
%{_texmfdistdir}/tex/latex/asaetr/asaesub.sty
%{_texmfdistdir}/tex/latex/asaetr/asaetr.cls
%{_texmfdistdir}/tex/latex/asaetr/asaetr.sty
%doc %{_texmfdistdir}/doc/latex/asaetr/MANIFEST
%doc %{_texmfdistdir}/doc/latex/asaetr/asaetr.bib
%doc %{_texmfdistdir}/doc/latex/asaetr/asaetr.pdf
%doc %{_texmfdistdir}/doc/latex/asaetr/asaetr.tex
%doc %{_texmfdistdir}/doc/latex/asaetr/cmcscsl10.mf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
