%define		pnetlib_version 0.6.4

Summary:	The ANSI compatible C library for IL
Summary(pl):	Zgodna z ANSI biblioteka C dla IL
Name:		pnetC
Version:	0.6.4
Release:	3
License:	LGPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	46968212ea6aebbbfee29666c49fea03
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pnet-compiler-c = %{version}
BuildRequires:	pnet-compiler-csharp = %{version}
BuildRequires:	pnetlib-base = %{pnetlib_version}
Requires:	pnetlib-base = %{pnetlib_version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of the pnetC project is to create an ANSI-compatible C
library, that can be compiled down to IL using Portable.NET's "cscc"
compiler.

%description -l pl
Celem projektu pnetC jest stworzenie zgodnej z ANSI C biblioteki,
która mo¿e byæ skompilowana do IL korzystaj±c z dostarczanego przez
Portable.NET kompilatora cscc.

%package devel
Summary:	Headers for pnet C library
Summary(pl):	Pliki nag³ówkowe dla biblioteki pnet C
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	pnet-compiler-c

%description devel
These are the header files required to build programs with the C
backend to cscc.

%description devel -l pl
Pliki nag³ówkowe potrzebne do budowania programów korzystaj±c z
nak³adki C na cscc.

%prep
%setup -q

%build
%{__aclocal}
%{__automake} --ignore-deps
%{__autoconf}
%configure
%{__make}
%{__make} check

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/cscc/lib/*

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*
%{_datadir}/cscc/include
