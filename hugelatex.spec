Summary:	Temporary package to provide hugelatex (latex with increased capacities)
Summary(pl):	Tymczasowy pakiet, który zawiera hugelatex (latexa o zwiêkszonych mo¿liwo¶ciach)
Name:		hugelatex
Version:	0
Release:	4
License:	GPL
Group:		Applications/Publishing/SGML
#Source0:
BuildRequires:	tetex >= 0.9
BuildRequires:	tetex-latex >= 0.9
BuildRequires:	tetex-tex-babel
BuildRequires:	tetex-tex-ruhyphen
BuildRequires:	tetex-tex-ukrhyph
BuildRequires:	tetex-csplain
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	tetex >= 1.0.7-2, tetex-latex >= 1.0.7-2

%description
Temporary package to provide hugelatex

%description -l pl
Tymczasowy pakiet zawieraj±cy hugelatex.

%prep
#%setup -q -n jadetex
#%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/texmf/web2c,%{_bindir}}

cp %{_datadir}/texmf/tex/latex/config/* $RPM_BUILD_ROOT/
(cd $RPM_BUILD_ROOT; tex -ini -progname=hugelatex latex.ini)
cp $RPM_BUILD_ROOT/latex.fmt $RPM_BUILD_ROOT/%{_datadir}/texmf/web2c/%{name}.fmt
ln -s %{_bindir}/tex $RPM_BUILD_ROOT%{_bindir}/%{name}

%post
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%postun
[ -x %{_bindir}/texhash ] && /usr/bin/env - %{_bindir}/texhash 1>&2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/texmf/web2c/*
%attr(755,root,root) %{_bindir}/*
