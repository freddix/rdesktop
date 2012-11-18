Summary:	RDP client for accessing Windows NT Terminal Server
Name:		rdesktop
Version:	1.7.1
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.sourceforge.net/rdesktop/%{name}-%{version}.tar.gz
# Source0-md5:	c4b39115951c4a6d74f511c99b18fcf9
URL:		http://www.rdesktop.org/
BuildRequires:	libao-devel
BuildRequires:	openssl-devel
BuildRequires:	xorg-libX11-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
rdesktop is an open source client for Windows NT or Windows 2000
Terminal Server, capable of natively speaking its Remote Desktop
Protocol (RDP) in order to present the user's NT desktop. Unlike
Citrix ICA, no server extensions are required.

%prep
%setup -q

%build
%configure \
	--with-ipv6		\
	--with-libao		\
	--with-sound=libao
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/
%attr(755,root,root) %{_bindir}/rdesktop
%{_datadir}/rdesktop
%{_mandir}/man1/rdesktop.1*

