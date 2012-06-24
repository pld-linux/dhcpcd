# conditional build:
# _without_embed - don't build uClibc version
%define	ver	1.3.20-pl0
Summary:	DHCP Client Daemon
Summary(de):	DHCPC-D�mon
Summary(fr):	D�mon DHCPC
Summary(pl):	Klient (daemon) DHCP
Summary(tr):	DHCPC sunucu s�re�i (daemon)
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
Computers, auf dem es l�uft Es versucht, die Verleihzeit gem�� RFC1541
bzw. draft-ietf-dhc-dhcp-09 zu verl�ngern.

%description -l fr
dhcpcd est une implantation du client DHCP sp�cifi� dans les
draft-ietf-dhc-dhcp-09 (sans l'option -r) et RFC1541 (avec l'option -r).

Il obtient l'information sur l'h�te (adresse IP, masque r�seau,
adresse de diffusion, etc.) � partir d'un serveur DHCP et configure
l'interface r�seau de la machine sur laquelle il tourne. Il essaie
aussi de renouveler le � lease time � selon les RFC1541 ou
draft-ietf-dhc-dhcp-09.

%description -l pl
dhcpd jest implementacja klienta DHCP, opisan� w
draft-ietf-dhc-dhcp-09 (kiedy nie podaje si� opcji -r) oraz RFC1544
(kiedy podaje si� opcj� -r).

Pobiera on informacj� o komputerze (adres IP, maska sieci, adres
rozg�oszeniowy itd.) i konfiguruje interfejs sieciowy maszyny, na
kt�rej jest uruchomiony. Pr�buje r�wnie� od�wiezy� czas przestoju
zgodnie z RFC1541 oraz draft-ietf-dhc-dhcp-09.

%description -l tr
Makina bilgilerini (IP adresi, a� maskesi, yay�n adresi, vb.) bir DHCP
sunucusundan al�r ve �zerinde �al��t��� makinan�n a� aray�z�n�
ayarlar. Ayr�ca RFC1541 veya draft-ietf-dhc-dhcp-09'a uygun olarak,
kira zaman�n� (lease time) yenilemeye �al���r.

%package embed
Summary:	dhcpcd for bootdisk
Group:		Networking/Daemons

%description embed
dhcpcd for bootdisk.

%description embed -l pl
dhcpcd na bootkietk�.

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
