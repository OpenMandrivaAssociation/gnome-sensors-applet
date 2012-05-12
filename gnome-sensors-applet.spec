Name: 	 	gnome-sensors-applet
Summary: 	Detailed hardware monitoring applet for GNOME2
Version: 	3.0.0
Release: 	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://sensors-applet.sourceforge.net/
Source0:	http://downloads.sourceforge.net/sensors-applet/sensors-applet-%{version}.tar.gz

BuildRequires:	gnome-doc-utils
BuildRequires:	intltool
BuildRequires:	xsltproc
BuildRequires:  perl-XML-Parser
BuildRequires:	libatasmart-devel
BuildRequires:	libbonobo-activation-devel
BuildRequires:	dbus-glib-devel
BuildRequires:	libGConf2-devel GConf2
BuildRequires:	libgnome2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	libnotify-devel
BuildRequires:	gnome-panel-devel
BuildRequires:	gnomeui2-devel

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
%setup -q -n sensors-applet-%{version}

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
%find_lang sensors-applet

%files -f sensors-applet.lang
%doc AUTHORS ChangeLog NEWS README TODO
%{_libdir}/sensors-applet
%{_libdir}/bonobo/servers/*
%{_datadir}/gnome-2.0/ui/*
%{_datadir}/pixmaps/*
%{_datadir}/gnome/help/sensors-applet
%{_datadir}/icons/hicolor/*/*/*.png
%{_libdir}/*.so.*

%files devel
%{_includedir}/sensors-applet/*.h
%{_libdir}/*.so

