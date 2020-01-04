%define _disable_rebuild_configure 1
%define url_ver	%(echo %{version}|cut -d. -f1,2)

Name:		gnome-robots
Version:	3.34.1
Release:	1
Summary:	GNOME Robots game
License:	GPLv2+ and GFDL
Group:		Games/Arcade
URL:		https://wiki.gnome.org/Robots
Source0:	https://download.gnome.org/sources/%{name}/%{url_ver}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gtk+-3.0) >= 3.4.0
BuildRequires:	pkgconfig(libcanberra-gtk3) >= 0.26
BuildRequires:	pkgconfig(librsvg-2.0) >= 2.32.0
BuildRequires:  pkgconfig(gsound)
BuildRequires:  cmake
BuildRequires:	intltool > 0.50
BuildRequires:	itstool
BuildRequires:	libxml2-utils
BuildRequires:	pkgconfig(libgnome-games-support-1)
BuildRequires:  meson
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
%meson
%meson_build

%install
%meon_install

%find_lang %{name} --with-gnome

%files -f %{name}.lang
%doc COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/glib-2.0/schemas/org.gnome.robots.gschema.xml
%{_datadir}/%{name}
%{_iconsdir}/*/*/*/*
%{_mandir}/man6/%{name}.6*
%{_datadir}/metainfo/%{name}.appdata.xml


