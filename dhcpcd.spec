Summary: DHCPC Daemon
Name: dhcpcd
%define	version 1.3.17pl2
Version: %{version}
Release: 1
Copyright: GPL
Group: System Environment/Daemons
Source: ftp://sunsite.unc.edu/pub/Linux/system/network/daemons/dhcpcd-1.3.17-pl2.tar.gz
Patch: dhcpcd-1.3.17-misc.patch
#Patch1: dhcpcd-0.65-glibc.patch
#Patch2: dhcpcd-0.65-buffer.patch
#Patch3: dhcpcd-0.65-align.patch
Patch4: dhcpcd-0.70-rtup.patch
BuildRoot: /var/tmp/%{name}-root

%description
dhcpcd is an implementation of the DHCP  client  specified in
draft-ietf-dhc-dhcp-09  (when  -r option is not speci- fied) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask,  broad- cast  address,
etc.) from a DHCP server and configures the network interface of the
machine on which it  is  running.  It also tries to renew the lease time
according to RFC1541 or draft-ietf-dhc-dhcp-09.

%description - pl
dhcpd jest implementacja klienta DHCP, opisan± w draft-ietf-dhc-dhcp-09
(kiedy nie podaje siê opcji -r) oraz RFC1544 (kiedy podaje siê opcjê -r).

Pobiera on informacjê o komputerze (adres IP, maska sieci, adres rozg³oszeniowy
itd.) i konfiguruje interfejs sieciowy maszyny, na której jest uruchomiony.
Próbuje równie¿ od¶wiezyæ czas przestoju zgodnie z RFC1541 oraz 
draft-ietf-dhc-dhcp-09.

%prep
%setup -q -n dhcpcd-1.3.17-pl2
%patch0 -p1 -b .misc
#%patch1 -p1 -b .glibc
#%patch2 -p1 -b .buffer
#%patch3 -p1 -b .align
#%patch4 -p1 -b .rtup 

%build
make RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin $RPM_BUILD_ROOT/usr/man/man8

install -s -m 755 dhcpcd $RPM_BUILD_ROOT/sbin/dhcpcd
install -m 644 dhcpcd.8 $RPM_BUILD_ROOT/usr/man/man8/dhcpcd.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/sbin/dhcpcd
/usr/man/man8/dhcpcd.8
