%global tl_name keyindex
%global tl_revision 50828

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Index entries by key lookup
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/keyindex
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyindex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyindex.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/keyindex.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides functionality for producing an index without
directly entering index entries into the text using the \index command,
but instead by looking up short keys and printing a predefined string in
the main text and adding a corresponding index entry. The standard use
case is the production of an index of names.

