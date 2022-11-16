Name:		texlive-fiziko
Version:	61944
Release:	1
Summary:	A MetaPost library for physics textbook illustrations
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/fiziko
License:	gpl3+ cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fiziko.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/fiziko.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This MetaPost library was initially written to automate some
elements of black and white illustrations for a physics
textbook. It provides functions to draw things like lines of
variable width, shaded spheres, and tubes of different kinds,
which can be used to produce images of a variety of objects.
The library also contains functions to draw some objects
constructed from these primitives.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/metapost/fiziko
%doc %{_texmfdistdir}/doc/metapost/fiziko

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
