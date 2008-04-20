%define rel 1
%define release %mkrel %rel

Name: ctorrent
Version: 3.3
Release: %release
Summary: Fast and small BitTorrent Client program written in C/C++
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPL
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
