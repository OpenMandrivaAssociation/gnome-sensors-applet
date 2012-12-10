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



%changelog
* Sat May 12 2012 Matthew Dawkins <mattydaw@mandriva.org> 3.0.0-1
+ Revision: 798378
- new release 3.0.0

* Wed Apr 20 2011 Funda Wang <fwang@mandriva.org> 2.2.7-1
+ Revision: 656099
- new version 2.2.7

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.2.5-2mdv2011.0
+ Revision: 610945
- rebuild

* Sat Nov 21 2009 Funda Wang <fwang@mandriva.org> 2.2.5-1mdv2010.1
+ Revision: 468540
- New version 2.2.5

* Fri Oct 02 2009 Frederic Crozat <fcrozat@mandriva.com> 2.2.3-4mdv2010.0
+ Revision: 452693
- Disable lm-sensors (Mdv bug #53418)

* Thu Oct 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 2.2.3-3mdv2010.0
+ Revision: 452333
- rebuild for new libsensors

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Mar 15 2009 Emmanuel Andry <eandry@mandriva.org> 2.2.3-1mdv2009.1
+ Revision: 355483
- BR libglade2-devel
- BR libgnomeui2-devel
- BR intltool
- New version 2.2.3
- use rarian, scrollkeeper is dead
- diff p1 to fix linkage
- diff p2 to fix string format not literal

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Feb 04 2008 Frederic Crozat <fcrozat@mandriva.com> 2.2.1-2mdv2008.1
+ Revision: 162005
- Patch0:  fix location of applet, caused by libdir == libexecdir (Mdv bug #37154)

* Wed Dec 26 2007 Funda Wang <fwang@mandriva.org> 2.2.1-1mdv2008.1
+ Revision: 137903
- New version 2.2.1

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Dec 13 2007 Jérôme Soyer <saispo@mandriva.org> 2.0.1-1mdv2008.1
+ Revision: 119278
- New release 2.0.1


* Wed Nov 22 2006 Jérôme Soyer <saispo@mandriva.org> 1.7.10-1mdv2007.0
+ Revision: 86061
- New release 1.7.10
- Import gnome-sensors-applet

* Sat Sep 02 2006 Götz Waschk <waschk@mandriva.org> 1.7.8-1mdv2007.0
- rebuild for new clean_icon_cache macro

* Fri Sep 01 2006 G�tz Waschk <waschk@mandriva.org> 1.7.8-2mdv2007.0
- handle scrollkeeper
- remove icon cache, it doesn't belong here

* Fri Aug 25 2006 Jerome Soyer <saispo@mandriva.org> 1.7.8-1mdv2007.0
- New release 1.7.8

* Wed Aug 23 2006 Jerome Soyer <saispo@mandriva.org> 1.7.7-1mdv2007.0
- New release 1.7.7

* Tue Aug 08 2006 Jerome Soyer <saispo@mandriva.org> 1.7.6-1mdv2007.0
- New release 1.7.6

* Tue Jul 25 2006 Jerome Soyer <saispo@mandriva.org> 1.7.5-1mdv2007.0
- New release 1.7.5

* Sun Apr 16 2006 Austin Acton <austin@mandriva.org> 1.6.1-1mdk
- New release 1.6.1

* Sun Oct 02 2005 Nicolas L�cureuil <neoclust@mandriva.org> 1.5-2mdk
- BuildRequires fix

* Sun Oct 02 2005 Austin Acton <austin@mandriva.org> 1.5-1mdk
- New release 1.5

* Fri Jul 08 2005 Austin Acton <austin@mandriva.org> 1.2-1mdk
- New release 1.2

* Sat Jul 02 2005 Austin Acton <austin@mandriva.org> 1.0-1mdk
- New release 1.0

* Sun Jun 05 2005 Austin Acton <austin@mandriva.org> 0.7.3-1mdk
- New release 0.7.3

* Wed Apr 20 2005 Austin Acton <austin@mandrake.org> 0.7.2-1mdk
- New release 0.7.2

* Tue Apr 05 2005 Austin Acton <austin@mandrake.org> 0.7.1-1mdk
- New release 0.7.1

* Thu Mar 10 2005 Austin Acton <austin@mandrake.org> 0.7-1mdk
- 0.7

* Sun Feb 20 2005 Austin Acton <austin@mandrake.org> 0.6.2-1mdk
- 0.6.2

* Wed Feb 16 2005 Austin Acton <austin@mandrake.org> 0.6.1-1mdk
- 0.6.1

* Sat Feb 05 2005 Austin Acton <austin@mandrake.org> 0.6.0-1mdk
- 0.6.0

* Tue Feb 01 2005 Austin Acton <austin@mandrake.org> 0.5.0-1mdk
- 0.5.0

* Mon Jan 31 2005 Austin Acton <austin@mandrake.org> 0.4.0-1mdk
- 0.4.0

* Sat Jan 29 2005 Austin Acton <austin@mandrake.org> 0.3.0-1mdk
- 0.3.0

* Tue Jan 25 2005 Austin Acton <austin@mandrake.org> 0.2.2-2mdk
- add TODO at author's request

* Mon Jan 24 2005 Austin Acton <austin@mandrake.org> 0.2.2-1mdk
- 0.2.2

* Mon Jan 17 2005 Austin Acton <austin@mandrake.org> 0.1-1mdk
- initial package

