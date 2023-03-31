Name:		texlive-keyindex
Version:	50828
Release:	2
Summary:	Index entries by key lookup
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/keyindex
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyindex.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyindex.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/keyindex.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides functionality for producing an index
without directly entering index entries into the text using the
\index command, but instead by looking up short keys and
printing a predefined string in the main text and adding a
corresponding index entry. The standard use case is the
production of an index of names.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/keyindex
%{_texmfdistdir}/tex/latex/keyindex
%doc %{_texmfdistdir}/doc/latex/keyindex

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
