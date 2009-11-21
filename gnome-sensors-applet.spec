%define name	gnome-sensors-applet
%define version 2.2.5
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Detailed hardware monitoring applet for GNOME2
Version: 	%{version}
Release: 	%{release}

Source:		http://downloads.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz
# (fc) 2.2.1-2mdv fix location of applet, caused by libdir == libexecdir (Mdv bug #37154)
Patch0:		sensors-applet-2.2.1-fixlibdir.patch
Patch1:		sensors-applet-2.2.3-fix-linkage.patch
URL:		http://sensors-applet.sourceforge.net/
License:	GPLv2+
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libpanel-applet-2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:	libnotify-devel
BuildRequires:  rarian
BuildRequires:  gnome-doc-utils
BuildRequires:	libxslt-proc
BuildRequires:	intltool
BuildRequires:	libgnomeui2-devel
BuildRequires:	libglade2-devel
Requires(post): rarian
Requires(postun): rarian

%description
GNOME Sensors Applet is an applet for the GNOME Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds and
voltage readings under Linux.

Interfaces via the Linux kernel i2c modules.

%package devel
Group:	Development/GNOME and GTK+
Summary: Development files for gnome-sensors-applet
Requires: %name = %version

%description devel
This package contains development files for gnome-sensors-applet.

%prep
%setup -q -n sensors-applet-%version
%patch0 -p1 -b .fixlibdir
%patch1	-p0 -b .fixlinkage

%build

#disable lm-sensors, not used with kernel 2.6 (Mdv bug #53418)
%configure2_5x --disable-scrollkeeper --enable-libnotify --without-libsensors --disable-static
%make

%install
rm -rf %{buildroot}
mkdir -p %buildroot%{_libdir}/sensors-applet/plugins
%makeinstall_std
%find_lang sensors-applet

%clean
rm -rf %{buildroot}

%post
%update_icon_cache hicolor
%update_scrollkeeper

%postun
%clean_icon_cache hicolor
%clean_scrollkeeper

%files -f sensors-applet.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/sensors-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome/help/sensors-applet
%dir %{_datadir}/omf/sensors-applet
%{_datadir}/omf/sensors-applet/*-C.omf
%_datadir/icons/hicolor/*/*/*.png
%_libdir/*.so.*

%files devel
%defattr(-,root,root)
%_includedir/sensors-applet/*.h
%_libdir/*.la
%_libdir/*.so

