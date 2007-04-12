%define name	gnome-sensors-applet
%define version 1.7.10
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Detailed hardware monitoring applet for GNOME2
Version: 	%{version}
Release: 	%{release}

Source:		sensors-applet-%{version}.tar.bz2
URL:		http://sensors-applet.sourceforge.net/
License:	GPL
Group:		Graphical desktop/GNOME
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	libpanel-applet-2-devel
BuildRequires:  perl-XML-Parser
BuildRequires:  scrollkeeper
BuildRequires:  gnome-doc-utils libxslt-proc
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
GNOME Sensors Applet is an applet for the GNOME Panel to display readings
from hardware sensors, including CPU and system temperatures, fan speeds and
voltage readings under Linux.

Interfaces via the Linux kernel i2c modules.

%prep
%setup -q -n sensors-applet-%version

%build
%configure2_5x --disable-scrollkeeper --prefix=/usr
%make
										
%install
rm -rf $RPM_BUILD_ROOT
%makeinstall
rm -f %buildroot%_datadir/icons/hicolor/icon-theme.cache
%find_lang sensors-applet

%clean
rm -rf $RPM_BUILD_ROOT

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


