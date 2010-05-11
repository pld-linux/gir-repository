#
# TODO:
#   - fix building with clutter >= 1.0, note: clutter-cairo
#     was obsoleted by clutter
#
Summary:	GObject Introspection repository
Summary(pl.UTF-8):	Repozytorium GObject Introspection
Name:		gir-repository
Version:	0.6.5
Release:	8
License:	GPL v2
Group:		Development/Libraries
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gir-repository/0.6/%{name}-%{version}.tar.bz2
# Source0-md5:	f161fa1ae161e81117af6f4bb79bf344
Patch0:		%{name}-gconf2path.patch
Patch1:		%{name}-makefile.patch
Patch2:		%{name}-pango.patch
Patch3:		%{name}-gstreamer-new.patch
URL:		http://live.gnome.org/GObjectIntrospection
BuildRequires:	GConf2-devel >= 2.0
BuildRequires:	atk-devel >= 1:1.12.0
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake
BuildRequires:	avahi-gobject-devel >= 0.6
BuildRequires:	babl-devel
#BuildRequires:	clutter-devel >= 0.8
#BuildRequires:	clutter-cairo-devel >= 0.8
#BuildRequires:	clutter-gtk-devel >= 0.8
BuildRequires:	dbus-glib-devel
BuildRequires:	glibc-misc
BuildRequires:	gnome-keyring-devel
BuildRequires:	gnome-menus-devel
BuildRequires:	gobject-introspection-devel >= 0.6.5
BuildRequires:	goocanvas-devel
BuildRequires:	gssdp-devel
BuildRequires:	gtk+2-devel >= 2:2.12.0
BuildRequires:	gtk-webkit-devel >= 1.0
BuildRequires:	gtksourceview2-devel
BuildRequires:	gupnp-devel
BuildRequires:	libnotify-devel
BuildRequires:	libsoup-devel >= 2.4
BuildRequires:	libtool
BuildRequires:	libunique-devel >= 1.0.0
BuildRequires:	libwnck-devel
BuildRequires:	nautilus-devel
BuildRequires:	openjpeg-devel
BuildRequires:	pango-devel >= 1:1.26.0
BuildRequires:	pkgconfig
BuildRequires:	poppler-glib-devel >= 0.8
BuildRequires:	vte-devel
# gnio ???
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Introspection system for GNOME libraries; see the
gobject-introspection package.

%description -l pl.UTF-8
System obserwacji dla bibliotek GNOME - więcej w pakiecie
gobject-introspection.

%package devel
Summary:	Development files for gir-repository
Summary(pl.UTF-8):	Pliki programistyczne dla gir-repository
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gobject-introspection-devel >= 0.6.5

%description devel
Development files for gir-repository.

%description devel -l pl.UTF-8
Pliki programistyczne dla gir-repository.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
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

for file in Atk-1.0 Unique-1.0 Gdk-2.0 GdkPixbuf-2.0 GMenu-2.0 Gtk-2.0 \
	    JSCore-1.0 WebKit-1.0 Wnck-1.0; do
    rm $RPM_BUILD_ROOT%{_libdir}/girepository-1.0/$file.typelib
    rm $RPM_BUILD_ROOT%{_datadir}/gir-1.0/$file.gir
done

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
