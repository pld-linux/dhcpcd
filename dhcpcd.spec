Summary:	DHCP Client Daemon
Summary(pl):	Klient (daemon) DHCP
Name:		dhcpcd
Version:	1.3.18pl7
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(pl):	Sieciowe/Serwery
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/%{name}-1.3.18-pl7.tar.gz
Patch0:		dhcpcd-configure.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
dhcpcd is an implementation of the DHCP client specified in
draft-ietf-dhc-dhcp-09 (when -r option is not speci- fied) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask, broad- cast address,
etc.) from a DHCP server and configures the network interface of the
machine on which it is running. It also tries to renew the lease time
according to RFC1541 or draft-ietf-dhc-dhcp-09.

%description -l pl
dhcpd jest implementacja klienta DHCP, opisan± w draft-ietf-dhc-dhcp-09
(kiedy nie podaje siê opcji -r) oraz RFC1544 (kiedy podaje siê opcjê -r).

Pobiera on informacjê o komputerze (adres IP, maska sieci, adres
rozg³oszeniowy itd.) i konfiguruje interfejs sieciowy maszyny, na której
jest uruchomiony. Próbuje równie¿ od¶wiezyæ czas przestoju zgodnie z
RFC1541 oraz draft-ietf-dhc-dhcp-09.

%prep
%setup -q -n dhcpcd-1.3.18-pl7
%patch -p1

%build
LDFLAGS="-s"; export LDFLAGS
autoconf
%configure
make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}/dhcpc

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/* \
	README AUTHORS ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,AUTHORS,ChangeLog,NEWS}.gz
%dir %{_sysconfdir}/dhcpc
%attr(755,root,root) %{_sbindir}/dhcpcd
%{_mandir}/man8/dhcpcd.8.gz
