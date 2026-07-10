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
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A class and BibTeX style for submissions to the Transactions of the
American Society of Agricultural Engineers. Also included is the
Metafont source of a slanted Computer Modern Caps and Small Caps font.

