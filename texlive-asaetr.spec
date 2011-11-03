# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/asaetr
# catalog-date 2009-04-30 00:32:08 +0200
# catalog-license pd
# catalog-version 1.0a
Name:		texlive-asaetr
Version:	1.0a
Release:	1
Summary:	Transactions of the ASAE
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/asaetr
License:	PD
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asaetr.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/asaetr.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
A class and BibTeX style for submissions to the Transactions of
the American Society of Agricultural Engineers. Also included
is the MetaFont source of a slanted Computer Modern Caps and
Small Caps font.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar bibtex tex doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
