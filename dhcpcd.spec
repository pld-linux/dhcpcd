%define	ver	1.3.20-pl0
Summary:	DHCP Client Daemon
Summary(de):	DHCPC-Dämon
Summary(fr):	Démon DHCPC
Summary(pl):	Klient (daemon) DHCP
Summary(tr):	DHCPC sunucu süreçi (daemon)
Name:		dhcpcd
Version:	%(echo %{ver} | sed -e "s#-##")
Release:	2
License:	GPL
Vendor:		Sergei Viznyuk <sv@phystech.com>
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://www.phystech.com/ftp/%{name}-%{ver}.tar.gz
Patch0:		%{name}-configure.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%if %{?BOOT:1}%{!?BOOT:0}
#BuildRequires:	glibc-static
%endif

%define		_sbindir	/sbin

%description
dhcpcd is an implementation of the DHCP client specified in
draft-ietf-dhc-dhcp-09 (when -r option is not speci- fied) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask, broad- cast
address, etc.) from a DHCP server and configures the network interface
of the machine on which it is running. It also tries to renew the
lease time according to RFC1541 or draft-ietf-dhc-dhcp-09.

%description -l de
dhcpcd ist eine Implementierung des DHCP-Client, spezifiziert in
draft-ietf-dhc-dhcp-09 (wenn -r option nicht angegeben) und RFC1541
(wenn -r option angegeben).

Es bezieht die Host-Infos (IP-Adresse, Netmask, Broadcast-Adresse,
usw.) von einem DHCP-Server und konfiguriert die Netzschnittstelle des
Computers, auf dem es läuft Es versucht, die Verleihzeit gemäß RFC1541
bzw. draft-ietf-dhc-dhcp-09 zu verlängern.

%description -l fr
dhcpcd est une implantation du client DHCP spécifié dans les
draft-ietf-dhc-dhcp-09 (sans l'option -r) et RFC1541 (avec l'option -r).

Il obtient l'information sur l'hôte (adresse IP, masque réseau,
adresse de diffusion, etc.) à partir d'un serveur DHCP et configure
l'interface réseau de la machine sur laquelle il tourne. Il essaie
aussi de renouveler le « lease time » selon les RFC1541 ou
draft-ietf-dhc-dhcp-09.

%description -l pl
dhcpd jest implementacja klienta DHCP, opisan± w
draft-ietf-dhc-dhcp-09 (kiedy nie podaje siê opcji -r) oraz RFC1544
(kiedy podaje siê opcjê -r).

Pobiera on informacjê o komputerze (adres IP, maska sieci, adres
rozg³oszeniowy itd.) i konfiguruje interfejs sieciowy maszyny, na
której jest uruchomiony. Próbuje równie¿ od¶wiezyæ czas przestoju
zgodnie z RFC1541 oraz draft-ietf-dhc-dhcp-09.

%description -l tr
Makina bilgilerini (IP adresi, að maskesi, yayýn adresi, vb.) bir DHCP
sunucusundan alýr ve üzerinde çalýþtýðý makinanýn að arayüzünü
ayarlar. Ayrýca RFC1541 veya draft-ietf-dhc-dhcp-09'a uygun olarak,
kira zamanýný (lease time) yenilemeye çalýþýr.

%package BOOT
Summary:	dhcpcd for bootdisk
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery

%description BOOT
dhcpcd for bootdisk.

%prep
%setup -q -n %{name}-%{ver}
%patch -p1

%build
aclocal
autoconf
automake -a -c
%if %{?BOOT:1}%{!?BOOT:0}
%configure
%{__make} \
	CFLAGS="-m386 -I/usr/lib/bootdisk%{_includedir} -Os" \
	LDFLAGS="-nostdlib -s" \
	LIBS="%{_libdir}/bootdisk%{_libdir}/crt0.o %{_libdir}/bootdisk%{_libdir}/libc.a -lgcc"
mv -f %{name} %{name}-BOOT
%{__make} distclean
rm -f config.cache
%endif

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/dhcpc

%if %{?BOOT:1}%{!?BOOT:0}
install -d $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_sbindir}
install %{name}-BOOT $RPM_BUILD_ROOT%{_libdir}/bootdisk%{_sbindir}/%{name}
%endif

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README AUTHORS ChangeLog NEWS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%dir %{_sysconfdir}/dhcpc
%attr(755,root,root) %{_sbindir}/dhcpcd
%{_mandir}/man8/dhcpcd.8*

%if %{?BOOT:1}%{!?BOOT:0}
%files BOOT
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/bootdisk%{_sbindir}/*
%endif
