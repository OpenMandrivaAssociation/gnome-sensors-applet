%define _disable_ld_no_undefined 1
%define git 20131013

%define major 0
%define libname %mklibname sensors-applet-plugin %{major}
%define devname %mklibname sensors-applet-plugin -d

Summary:	Detailed hardware monitoring applet for GNOME2
Name:		gnome-sensors-applet
Version:	3.0.0
Release:	2.%{git}.1
License:	GPLv2+
Group:		Graphical desktop/GNOME
Url:		http://sensors-applet.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sensors-applet/sensors-applet-%{version}-%{git}.tar.bz2
BuildRequires:	intltool
BuildRequires:	perl-XML-Parser
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	pkgconfig(libatasmart)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	pkgconfig(libpanelapplet-4.0)

%description
GNOME Sensors Applet is an applet for the GNOME Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds and
voltage readings under Linux.

Interfaces via the Linux kernel i2c modules.

%files -f sensors-applet.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/sensors-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.SensorsAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.SensorsApplet.panel-applet
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/pixmaps/*
%{_datadir}/sensors-applet/ui/SensorsApplet.xml

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	Shared library for gnome-sensors-applet
Group:		System/Libraries
Conflicts:	%{name} < 3.0.0-2

%description -n %{libname}
Shared library for gnome-sensors-applet.

%files -n %{libname}
%{_libdir}/libsensors-applet-plugin.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Development files for gnome-sensors-applet
Group:		Development/GNOME and GTK+
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Conflicts:	%{name}-devel < 3.0.0-2
Obsoletes:	%{name}-devel < 3.0.0-2

%description -n %{devname}
This package contains development files for gnome-sensors-applet.

%files -n %{devname}
%{_includedir}/sensors-applet/*.h
%{_libdir}/libsensors-applet-plugin.so

#----------------------------------------------------------------------------

%prep
%setup -qn sensors-applet-%{version}-%{git}

%build
autoreconf -fi
%configure2_5x \
	--disable-scrollkeeper \
	--enable-libnotify \
	--without-libsensors \
	--disable-static

%make

%install
mkdir -p %{buildroot}%{_libdir}/sensors-applet/plugins

%makeinstall_std

%find_lang sensors-applet --with-gnome

