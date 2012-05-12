%define _disable_ld_no_undefined 1

Name: 	 	gnome-sensors-applet
Summary: 	Detailed hardware monitoring applet for GNOME2
Version: 	3.0.0
Release: 	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://sensors-applet.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz

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

%package devel
Group:	Development/GNOME and GTK+
Summary: Development files for gnome-sensors-applet
Requires: %{name} = %{version}

%description devel
This package contains development files for gnome-sensors-applet.

%prep
%setup -qn sensors-applet-%{version}

%build

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

%files -f sensors-applet.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/*.so.0*
%{_libdir}/sensors-applet
%{_datadir}/dbus-1/services/org.gnome.panel.applet.SensorsAppletFactory.service
%{_datadir}/gnome-panel/4.0/applets/org.gnome.applets.SensorsApplet.panel-applet
%{_datadir}/icons/hicolor/*/*/*.png
%{_datadir}/pixmaps/*
%{_datadir}/sensors-applet/ui/SensorsApplet.xml

%files devel
%{_includedir}/sensors-applet/*.h
%{_libdir}/*.so

