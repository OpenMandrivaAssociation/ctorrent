%define rel 4
%define release %mkrel %rel

Name: ctorrent
Version: 3.3.2
Release: %release
Summary: Fast and small BitTorrent Client program written in C/C++
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPLv2
Group: Networking/File transfer
URL: http://www.rahul.net/dholmes/ctorrent/
Source0: http://www.rahul.net/dholmes/ctorrent/ctorrent-dnh%{version}.tar.gz
BuildRequires: openssl-devel

%description
CTorrent is a BitTorrent Client program written in C/C++ for FreeBSD and Linux.
Fast and small are CTorrent's two strengths.

This is the Enhanced CTorrent fork.

%prep
%setup -q -n ctorrent-dnh%version

%build
%configure2_5x
%make

%install 
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;
%makeinstall
    
%clean
[ "$RPM_BUILD_ROOT" != "/" ] && [ -d $RPM_BUILD_ROOT ] && rm -rf $RPM_BUILD_ROOT;

%files
%defattr(-,root,root)
%{_bindir}/%{name}
%doc AUTHORS ChangeLog NEWS README* VERSION


%changelog
* Tue Dec 06 2011 Götz Waschk <waschk@mandriva.org> 3.3.2-4mdv2012.0
+ Revision: 738115
- yearly rebuild

* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 3.3.2-3mdv2011.0
+ Revision: 610176
- rebuild

* Wed Apr 21 2010 Funda Wang <fwang@mandriva.org> 3.3.2-2mdv2010.1
+ Revision: 537462
- rebuild

* Thu Aug 07 2008 Götz Waschk <waschk@mandriva.org> 3.3.2-1mdv2009.0
+ Revision: 265707
- new version
- update license

* Sun Apr 20 2008 Götz Waschk <waschk@mandriva.org> 3.3-1mdv2009.0
+ Revision: 195920
- new version

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Sep 05 2007 Götz Waschk <waschk@mandriva.org> 3.2-1mdv2008.0
+ Revision: 79923
- switch to the Enhanced CTorrent fork

* Wed Jul 25 2007 Götz Waschk <waschk@mandriva.org> 1.3.4-4mdv2008.0
+ Revision: 55222
- Import ctorrent



* Thu Jul 20 2006 Götz Waschk <waschk@mandriva.org> 1.3.4-1mdv2007.0
- Rebuild

* Fri Mar 17 2006 Götz Waschk <waschk@mandriva.org> 1.3.4-3mdk
- rebuild for new openssl

* Thu May 19 2005 G�tz Waschk <waschk@mandriva.org> 1.3.4-2mdk
- mkrel

* Sun Feb 20 2005 G�tz Waschk <waschk@linux-mandrake.com> 1.3.4-1mdk
- initial mdk package

* Sat Dec 18 2004 - darix@irssi.org
- initial package
