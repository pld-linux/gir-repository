#
#
%define svn 20081122
Summary:	GObject Introspection repository
Name:		gir-repository
Version:	0.0
Release:	0.%{svn}.1
License:	GPLv2
Group:		Development/Libraries
Source0:	%{name}-%{svn}.tar.bz2
# Source0-md5:	8dbd2f7a3c8cb8522171c7d826b66345
Patch0:		%{name}-gconf2path.patch
URL:		http://live.gnome.org/GObjectIntrospection
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	intltool
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description

%prep
%setup -q -n %{name}
%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires
#%%{__intltoolize}
#%%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
# if not running libtool or automake, but config.sub is too old:
#cp -f /usr/share/automake/config.sub .
%configure
%{__make}

#%{__make} \
#	CFLAGS="%{rpmcflags}" \
#	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

%if %{with ldconfig}
%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig
%endif

%if %{with initscript}
%post init
/sbin/chkconfig --add %{name}
%service %{name} restart

%preun init
if [ "$1" = "0" ]; then
	%service -q %{name} stop
	/sbin/chkconfig --del %{name}
fi
%endif

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_libdir}/girepository/*.typelib
#%{_libdir}/libgirepo-Clutter-custom.a
#%{_libdir}/libgirepo-Clutter-custom.la
%{_libdir}/libgirepo-Clutter-custom.so
#%{_libdir}/libgirepo-Gdk-custom.a
#%{_libdir}/libgirepo-Gdk-custom.la
%{_libdir}/libgirepo-Gdk-custom.so
#%{_libdir}/libgirepo-Gtk-custom.a
#%{_libdir}/libgirepo-Gtk-custom.la
%{_libdir}/libgirepo-Gtk-custom.so
%{_pkgconfigdir}/gir-repository-1.0.pc
%{_datadir}/gir/*.gir
