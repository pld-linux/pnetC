Summary:	The ANSI compatible C library for IL
Summary(pl):	Zgodna z ANSI biblioteka C dla IL
Name:		pnetC
Version:	0.5.6
Release:	1
License:	LGPL
Vendor:		DotGNU
Group:		Libraries
Source0:	http://www.southern-storm.com.au/download/%{name}-%{version}.tar.gz
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pnet-interpreter
BuildRequires:	pnet-compiler >= 0.5.6
BuildRequires:	pnet-tools
#Requires:	pnet-interpreter
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The goal of the pnetC project is to create an ANSI-compatible C
library, that can be compiled down to IL using Portable.NET's "cscc"
compiler.

%description -l pl
Celem projektu pnetC jest stworzenie zgodnej z ANSI C biblioteki,
która mo¿e byæ skompilowana do IL korzystaj±c z dostarczanego przez
Portable.NET kompilatora cscc.

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
%{_libdir}/cscc/include
%{_libdir}/cscc/lib

%doc AUTHORS ChangeLog NEWS README doc/*
