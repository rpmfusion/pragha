Name:           pragha
Version:        0.8.0.2
Release:        1%{?dist}
Summary:        Lightweight GTK+ music manager

Group:          Applications/Multimedia
License:        GPLv3+
URL:            http://pragha.wikispaces.com/
Source0:        http://dissonance.googlecode.com/files/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  alsa-lib-devel >= 1.0.15 
BuildRequires:  dbus-glib-devel >= 0.74
BuildRequires:  gtk2-devel >= 2.16.0
BuildRequires:  flac-devel >= 1.2.1
BuildRequires:  libao-devel >= 0.8.8
BuildRequires:  libcddb-devel >= 1.2.1
BuildRequires:  libcdio-devel >= 0.78
BuildRequires:  libcurl-devel >= 7.18
BuildRequires:  libmad-devel >= 0.15
BuildRequires:  libmodplug-devel
BuildRequires:  libnotify-devel >= 0.4.4
BuildRequires:  libsndfile-devel >= 1.0.17
BuildRequires:  libvorbis-devel >= 1.2.0
BuildRequires:  sqlite-devel >= 3.4
BuildRequires:  taglib-devel >= 1.4
BuildRequires:  desktop-file-utils
BuildRequires:  gettext

%description
Pragha is is a lightweight GTK+ music manager that aims to be fast, bloat-free,
and light on memory consumption. It is written completely in C and GTK+. 

Pragha is a fork of Consonance Music Manager, discontinued by the original 
author.


%prep
%setup -q
# Fix spurious executable permissions
chmod 0644 ChangeLog src/*.{c,h}

%build
%configure
make %{?_smp_mflags} V=1


%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT INSTALL='install -p'
desktop-file-install                                       \
  --delete-original                                        \
  --remove-category=AudioVideo                             \
  --add-category=Audio                                     \
  --dir=${RPM_BUILD_ROOT}%{_datadir}/applications          \
  ${RPM_BUILD_ROOT}%{_datadir}/applications/%{name}.desktop
%find_lang %{name}
# remove duplicate docs
rm -rf ${RPM_BUILD_ROOT}%{_datadir}/%{name}/doc

%clean
rm -rf $RPM_BUILD_ROOT


%post
touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :
update-desktop-database &> /dev/null || :


%postun
if [ $1 -eq 0 ] ; then
    touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi
update-desktop-database &> /dev/null || :


%posttrans
gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f %{name}.lang
%defattr(-,root,root,-)
# FIXME add AUTHORS and README if not empty
%doc ChangeLog COPYING FAQ NEWS
%{_bindir}/pragha
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*x*/apps/%{name}.png
%{_datadir}/pixmaps/%{name}/
%{_datadir}/%{name}/
%{_mandir}/man1/pragha.1.*


%changelog
* Fri Jul 30 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0.2-1
- Update to 0.8.0.2
- Drop de.po patch, included upstream

* Fri Jul 30 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0.1-1
- Update to 0.8.0.1
- Add COPYING and NEWS to docs

* Thu Jul 29 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.8.0-1
- Update to 0.8.0

* Fri Jun 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.7.1-1
- Update to 0.7.7.1

* Fri Jun 25 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.7-1
- Update to 0.7.7

* Sat Jun 19 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.6-1
- Update to 0.7.6
- Remove upstreamed use-software-mixer.patch

* Fri Apr 22 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.4-1
- Update to 0.7.4

* Mon Mar 22 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.3-2
- Use software mixer by default to cope with pulseaudio
- Remove executable bits from docs

* Tue Mar 16 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.3-1
- Update to 0.7.3

* Sat Feb 20 2010 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.2-1
- Update to 0.7.2

* Wed Oct 28 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.1-1
- Upadte to 0.7.1

* Sat Oct 03 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.7.0-1
- Upadte to 0.7.0

* Sun Aug 09 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.3-1
- Upadte to 0.6.3

* Mon Jul 20 2009 Christoph Wickert <cwickert@fedoraproject.org> - 0.6.2.2-1
- Initial Fedora package
