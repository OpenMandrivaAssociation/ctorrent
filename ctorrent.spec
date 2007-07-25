%define rel 4
%define release %mkrel %rel
#fixed2
%{?!mkrel:%define mkrel(c:) %{-c: 0.%{-c*}.}%{!?_with_unstable:%(perl -e '$_="%{1}";m/(.\*\\D\+)?(\\d+)$/;$rel=${2}-1;re;print "$1$rel";').%{?subrel:%subrel}%{!?subrel:1}.%{?distversion:%distversion}%{?!distversion:%(echo $[%{mdkversion}/10])}}%{?_with_unstable:%{1}}%{?distsuffix:%distsuffix}%{?!distsuffix:mdk}}

Name: ctorrent
Version: 1.3.4
Release: %release
Summary: Fast and small BitTorrent Client program written in C/C++
BuildRoot: %{_tmppath}/%{name}-%{version}-build
License: GPL
Group: Networking/File transfer
URL: http://ctorrent.sourceforge.net/
Source0: http://prdownloads.sourceforge.net/ctorrent/ctorrent-%{version}.tar.bz2
BuildRequires: openssl-devel

%description
CTorrent is a BitTorrent Client program written in C/C++ for FreeBSD and Linux.
Fast and small are CTorrent's two strengths.

Authors:
--------
    YuHong <bsdi@sina.com>


%prep
%setup -q

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
%doc AUTHORS ChangeLog NEWS README VERSION
