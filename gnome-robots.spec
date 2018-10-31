%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-robots
Version:	3.18.1
Release:	2
Summary:	GNOME Robots game
License:	GPLv2+ and GFDL
Group:		Games/Arcade
URL:		https://wiki.gnome.org/Robots
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:	intltool > 0.50
BuildRequires:	itstool
BuildRequires:	libxml2-utils
Obsoletes:	gnobots2
Obsoletes:	gnobots2-extra-data
# For help
Requires:	yelp

%description
The classic game where you have to avoid a hoard of robots who are trying to
kill you. Each step you take brings them closer toward you. Fortunately they
aren't very smart and you also have a helpful teleportation gadget.

%prep
%setup -q

%build
%configure
%make

%install
%makeinstall_std

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.robots.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_mandir}/man6/%{name}.6*
%{_datadir}/appdata/%{name}.appdata.xml


%changelog
* Tue Feb 17 2015 wally <wally> 3.14.2-2.mga5
+ Revision: 815342
- require yelp for showing help

* Tue Nov 11 2014 ovitters <ovitters> 3.14.2-1.mga5
+ Revision: 796296
- new version 3.14.2

* Wed Oct 15 2014 umeabot <umeabot> 3.14.1-2.mga5
+ Revision: 750861
- Second Mageia 5 Mass Rebuild

* Fri Oct 10 2014 ovitters <ovitters> 3.14.1-1.mga5
+ Revision: 737811
- new version 3.14.1

* Mon Sep 22 2014 ovitters <ovitters> 3.14.0-1.mga5
+ Revision: 719183
- new version 3.14.0

* Tue Sep 16 2014 umeabot <umeabot> 3.13.92-2.mga5
+ Revision: 679753
- Mageia 5 Mass Rebuild

* Tue Sep 16 2014 ovitters <ovitters> 3.13.92-1.mga5
+ Revision: 676966
- new version 3.13.92

* Tue Aug 19 2014 ovitters <ovitters> 3.13.90-1.mga5
+ Revision: 665305
- new version 3.13.90

* Mon Jul 21 2014 ovitters <ovitters> 3.13.4-1.mga5
+ Revision: 655167
- new version 3.13.4

* Tue Jun 24 2014 ovitters <ovitters> 3.13.3-1.mga5
+ Revision: 639210
- new version 3.13.3

* Sat Jun 21 2014 ovitters <ovitters> 3.12.3-1.mga5
+ Revision: 638548
- new version 3.12.3

* Mon May 12 2014 ovitters <ovitters> 3.12.2-1.mga5
+ Revision: 622337
- new version 3.12.2

* Mon Apr 14 2014 ovitters <ovitters> 3.12.1-1.mga5
+ Revision: 614157
- new version 3.12.1

* Mon Mar 24 2014 ovitters <ovitters> 3.12.0-1.mga5
+ Revision: 608070
- new version 3.12.0

* Mon Mar 17 2014 ovitters <ovitters> 3.11.92-1.mga5
+ Revision: 604568
- new version 3.11.92

* Tue Feb 18 2014 fwang <fwang> 3.11.90-1.mga5
+ Revision: 594118
- update file list

  + ovitters <ovitters>
    - new version 3.11.90

* Wed Feb 05 2014 dams <dams> 3.11.3-1.mga5
+ Revision: 582987
- new version 3.11.3

* Tue Feb 04 2014 ovitters <ovitters> 3.10.2-1.mga5
+ Revision: 582472
- new version 3.10.2

* Sat Nov 09 2013 ovitters <ovitters> 3.10.0-3.mga4
+ Revision: 550166
- fix url

* Sat Oct 19 2013 umeabot <umeabot> 3.10.0-2.mga4
+ Revision: 536542
- Mageia 4 Mass Rebuild

* Mon Sep 23 2013 ovitters <ovitters> 3.10.0-1.mga4
+ Revision: 484535
- new version 3.10.0

* Tue Sep 17 2013 ovitters <ovitters> 3.9.92-1.mga4
+ Revision: 480501
- new version 3.9.92

* Wed Aug 21 2013 fwang <fwang> 3.9.90-1.mga4
+ Revision: 468764
- new version 3.9.90
- cleanup spec

* Sun Jun 09 2013 dams <dams> 3.8.1-3.mga4
+ Revision: 440875
- Better 'Obsoletes'

* Sun Jun 09 2013 dams <dams> 3.8.1-2.mga4
+ Revision: 440813
- Obsoletes 'gnome-games-extra-data'

* Sun Jun 09 2013 dams <dams> 3.8.1-1.mga4
+ Revision: 440763
- add 'libxml2-utils' as BR
- imported package gnome-robots

