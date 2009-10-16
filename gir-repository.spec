Summary:	GObject Introspection repository
Name:		gir-repository
Version:	0.6.5
Release:	1
License:	GPL v2
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gir-repository/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	f161fa1ae161e81117af6f4bb79bf344
Patch0:		%{name}-gconf2path.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-gstreamer-new.patch
URL:		http://live.gnome.org/GObjectIntrospection
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	avahi-gobject-devel
BuildRequires:	babl-devel
BuildRequires:	gnome-keyring-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel >= 0.6.4
BuildRequires:	goocanvas-devel
BuildRequires:	gssdp-devel
BuildRequires:	gstreamer-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtk-webkit-devel
BuildRequires:	gtksourceview2-devel
BuildRequires:	gupnp-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel
BuildRequires:	libtool
BuildRequires:	libunique-devel
BuildRequires:	libwnck-devel
BuildRequires:	poppler-glib-devel
BuildRequires:	vte-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Introspection system for GNOME libraries; see the
gobject-introspection package.

%package devel
Summary:	Libraries and headers for gir-repository
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gobject-introspection-devel

%description devel
Libraries and headers for gir-repository.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/Pango*.typelib
rm -rf $RPM_BUILD_ROOT%{_datadir}/gir-1.0/Pango*.gir

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/girepository-1.0/*.typelib
%attr(755,root,root) %{_libdir}/libgirepo-DBus-custom.so
%attr(755,root,root) %{_libdir}/libgirepo-Gdk-custom.so
%attr(755,root,root) %{_libdir}/libgirepo-Gtk-custom.so

%files devel
%defattr(644,root,root,755)
%{_datadir}/gir-1.0/*.gir
%{_libdir}/libgirepo-DBus-custom.la
%{_libdir}/libgirepo-Gdk-custom.la
%{_libdir}/libgirepo-Gtk-custom.la
