# conditional build:
# _without_embed - don't build uClibc version
%define	ver	1.3.20-pl0
Summary:	DHCP Client Daemon
Summary(de):	DHCPC-Dämon
Summary(fr):	Démon DHCPC
Summary(pl):	Klient (daemon) DHCP
Summary(tr):	DHCPC sunucu süreçi (daemon)
Name:		dhcpcd
Version:	%(echo %{ver} | sed -e "s#-##")
Release:	3
License:	GPL
Vendor:		Sergei Viznyuk <sv@phystech.com>
Group:		Networking/Daemons
Source0:	http://www.phystech.com/ftp/%{name}-%{ver}.tar.gz
Patch0:		%{name}-configure.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
%if %{!?_without_embed:1}%{?_without_embed:0}
BuildRequires:	uClibc-devel
BuildRequires:	uClibc-static
%endif

%define embed_path	/usr/lib/embed
%define embed_cc	%{_arch}-uclibc-cc
%define embed_cflags	%{rpmcflags} -Os

%define	_sbindir	/sbin

%description
dhcpcd is an implementation of the DHCP client specified in
draft-ietf-dhc-dhcp-09 (when -r option is not specified) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask, broadcast
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

%package embed
Summary:	dhcpcd for bootdisk
Group:		Networking/Daemons

%description embed
dhcpcd for bootdisk.

%description embed -l pl
dhcpcd na bootkietkê.

%prep
%setup -q -n %{name}-%{ver}
%patch -p1

%build
aclocal
autoconf
automake -a -c
%if %{!?_without_embed:1}%{?_without_embed:0}
%configure
%{__make} \
	CFLAGS="%{embed_cflags}" \
	CC=%{embed_cc}
mv -f %{name} %{name}-embed-shared
%{__make} \
	CFLAGS="%{embed_cflags}" \
	LDFLAGS="-static" \
	CC=%{embed_cc}
mv -f %{name} %{name}-embed-static
%{__make} distclean
rm -f config.cache
%endif

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}/dhcpc

%if %{!?_without_embed:1}%{?_without_embed:0}
install -d $RPM_BUILD_ROOT%{embed_path}/{shared,static}
install %{name}-embed-shared $RPM_BUILD_ROOT%{embed_path}/shared/%{name}
install %{name}-embed-static $RPM_BUILD_ROOT%{embed_path}/static/%{name}
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

%if %{!?_without_embed:1}%{?_without_embed:0}
%files embed
%defattr(644,root,root,755)
%attr(755,root,root) %{embed_path}/*/*
%endif
