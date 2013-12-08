Summary:	MateCORBA - a fork of GNOME's ORBit
Summary(pl.UTF-8):	MateCORBA - odgałęzienie ORBita z GNOME
Name:		mate-corba
Version:	1.4.1
Release:	1
License:	LGPL v2+ (libraries), GPL v2+
Group:		Libraries
Source0:	http://pub.mate-desktop.org/releases/1.4/%{name}-%{version}.tar.xz
# Source0-md5:	867d05e015b1a7fda957b4914b5f5bea
Patch0:		%{name}-am.patch
URL:		http://wiki.mate-desktop.org/mate-corba
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake >= 1:1.9
BuildRequires:	glib2-devel >= 1:2.8.0
BuildRequires:	gtk-doc >= 1.0
BuildRequires:	libIDL-devel >= 0.8.2
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.18
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	glib2 >= 1:2.8.0
Requires:	libIDL >= 0.8.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MateCORBA is a fork of GNOME's ORBit.

%description -l pl.UTF-8
MateCORBA to odgałęzienie ORBita z GNOME.

%package devel
Summary:	Header files for MateCORBA libraries
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek MateCORBA
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel >= 1:2.8.0
Requires:	libIDL-devel >= 0.8.2

%description devel
Header files for MateCORBA libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek MateCORBA.

%package static
Summary:	Static MateCORBA libraries
Summary(pl.UTF-8):	Statyczne biblioteki MateCORBA
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static MateCORBA libraries.

%description static -l pl.UTF-8
Statyczne biblioteki MateCORBA.

%package apidocs
Summary:	MateCORBA API documentation
Summary(pl.UTF-8):	Dokumentacja API MateCORBA
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
MateCORBA API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API MateCORBA.

%prep
%setup -q
%patch0 -p1

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# loadable module
%{__rm} $RPM_BUILD_ROOT%{_libdir}/matecorba-2.0/*.{la,a}
# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libMateCORBA*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/matecorba-idl-2
%attr(755,root,root) %{_bindir}/matecorba-ior-decode-2
%attr(755,root,root) %{_bindir}/matecorba-linc-cleanup-sockets
%attr(755,root,root) %{_bindir}/matecorba-typelib-dump
%attr(755,root,root) %{_libdir}/libMateCORBA-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMateCORBA-2.so.0
%attr(755,root,root) %{_libdir}/libMateCORBA-imodule-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMateCORBA-imodule-2.so.0
%attr(755,root,root) %{_libdir}/libMateCORBACosNaming-2.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libMateCORBACosNaming-2.so.0
%dir %{_libdir}/matecorba-2.0
%attr(755,root,root) %{_libdir}/matecorba-2.0/Everything_module.so
%{_datadir}/idl/matecorba-2.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/matecorba2-config
%attr(755,root,root) %{_libdir}/libMateCORBA-2.so
%attr(755,root,root) %{_libdir}/libMateCORBA-imodule-2.so
%attr(755,root,root) %{_libdir}/libMateCORBACosNaming-2.so
%{_libdir}/libname-matecorba-server-2.a
%{_includedir}/matecorba-2.0
%{_pkgconfigdir}/MateCORBA-2.0.pc
%{_pkgconfigdir}/MateCORBA-CosNaming-2.0.pc
%{_pkgconfigdir}/MateCORBA-idl-2.0.pc
%{_pkgconfigdir}/MateCORBA-imodule-2.0.pc
%{_aclocaldir}/MateCORBA2.m4

%files static
%defattr(644,root,root,755)
%{_libdir}/libMateCORBA-2.a
%{_libdir}/libMateCORBA-imodule-2.a
%{_libdir}/libMateCORBACosNaming-2.a

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/MateCORBA2
