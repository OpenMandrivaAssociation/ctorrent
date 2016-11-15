Summary:	Fast and small BitTorrent Client program written in C/C++
Name:		ctorrent
Version:	3.3.2
Release:	7
License:	GPLv2+
Group:		Networking/File transfer
Url:		http://www.rahul.net/dholmes/ctorrent/
Source0:	http://www.rahul.net/dholmes/ctorrent/%{name}-dnh%{version}.tar.gz
BuildRequires:	pkgconfig(openssl)

%description
CTorrent is a BitTorrent Client program written in C/C++ for FreeBSD and Linux.
Fast and small are CTorrent's two strengths.

This is the Enhanced CTorrent fork.

%files
%doc AUTHORS ChangeLog NEWS README* VERSION
%{_bindir}/%{name}

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-dnh%{version}
find . -perm 0600 | xargs chmod 0644

%build
%configure2_5x
%make

%install
%makeinstall_std


