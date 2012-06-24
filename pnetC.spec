Summary:	The ANSI compatible C library for IL
Summary(pl):	Zgodna z ANSI biblioteka C dla IL
Name:		pnetC
Version:	0.5.10
Release:	1
License:	LGPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
# Source0-md5:	31a95c990aa6d8b623b6858abf581159
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pnet-compiler-c = %{version}
BuildRequires:	pnetlib-base = %{version}
Requires:	pnetlib-base = %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of the pnetC project is to create an ANSI-compatible C
library, that can be compiled down to IL using Portable.NET's "cscc"
compiler.

%description -l pl
Celem projektu pnetC jest stworzenie zgodnej z ANSI C biblioteki,
kt�ra mo�e by� skompilowana do IL korzystaj�c z dostarczanego przez
Portable.NET kompilatora cscc.

%package devel
Summary:	Headers for pnet C library
Summary(pl):	Pliki nag��wkowe dla biblioteki pnet C
Group:		Development/Libraries
Requires:	%{name}
Requires:	pnet-compiler-c

%description devel
These are the header files required to build programs with the C
backend to cscc.

%description devel -l pl
Pliki nag��wkowe potrzebne do budowania program�w korzystaj�c z
nak�adki C na cscc.

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
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%{_libdir}/cscc/lib

%files devel
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README doc/*
%{_datadir}/cscc/include
