Summary:	DHCP Client Daemon
Summary(de):	DHCPC-Dämon
Summary(es):	Servidor DHCPC
Summary(fr):	Démon DHCPC
Summary(pl):	Klient (daemon) DHCP
Summary(pt_BR):	Servidor DHCPC
Summary(tr):	DHCPC sunucu süreçi (daemon)
Name:		dhcpcd
%define	ver	1.3.22-pl4
Version:	%(echo %{ver} | tr -d - )
Release:	2
License:	GPL v2
Group:		Networking/Daemons
Source0:	http://www.phystech.com/ftp/%{name}-%{ver}.tar.gz
# Source0-md5:	dd627a121e43835bead3ffef5b1a72fd
Patch0:		%{name}-configure.patch
Patch1:		%{name}-ntpdrift-66136.patch
Patch2:		%{name}-noMoFakery.patch
Patch3:		%{name}-noNISfakery.patch
Patch4:		%{name}-paths_fixes.patch
BuildRequires:	automake
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define	_sbindir	/sbin

%description
dhcpcd is an implementation of the DHCP client specified in
draft-ietf-dhc-dhcp-09 (when -r option is not specified) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask, broadcast address,
etc.) from a DHCP server and configures the network interface of the
machine on which it is running. It also tries to renew the lease time
according to RFC1541 or draft-ietf-dhc-dhcp-09.

%description -l de
dhcpcd ist eine Implementierung des DHCP-Client, spezifiziert in
draft-ietf-dhc-dhcp-09 (wenn -r option nicht angegeben) und RFC1541
(wenn -r option angegeben).

Es bezieht die Host-Infos (IP-Adresse, Netmask, Broadcast-Adresse,
usw.) von einem DHCP-Server und konfiguriert die Netzschnittstelle des
Computers, auf dem es läuft Es versucht, die Verleihzeit gemäß RFC1541
bzw. draft-ietf-dhc-dhcp-09 zu verlängern.

%description -l es
dhcpcd es una implementación del cliente DHCP especificado en
draft-ietf-dhc-dhcp-09 (cuando la opción -r no está especificada) y
RFC1541 (cuando la opción -r está especificada). Captura la
información del host (dirección IP, máscara de red, dirección de
broadcast, etc.) de un servidor DHCP y configura la interface de red
de la máquina donde esté ejecutando. También intenta renovar el tiempo
de alquiler de los direcciones de acuerdo con RFC1541 o
draft-ietf-dhc-dhcp-09.

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

%description -l pt_BR
dhcpcd é uma implementação do cliente DHCP especificado em
draft-ietf-dhc-dhcp-09 (quando a opção -r não é especificada) e
RFC1541 (quando a opção -r é especificada). Ele captura a informação
do host (endereço IP, máscara de rede, endereço de broadcast, etc.) de
um servidor DHCP e configura a interface de rede da máquina em que
está rodando. Ele também tenta renovar o tempo de aluguel dos
endereços de acordo com RFC1541 ou draft-ietf-dhc-dhcp-09.

%description -l tr
Makina bilgilerini (IP adresi, að maskesi, yayýn adresi, vb.) bir DHCP
sunucusundan alýr ve üzerinde çalýþtýðý makinanýn að arayüzünü
ayarlar. Ayrýca RFC1541 veya draft-ietf-dhc-dhcp-09'a uygun olarak,
kira zamanýný (lease time) yenilemeye çalýþýr.

%prep
%setup -q -n %{name}-%{ver}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
rm -f missing
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make} all \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_var}/lib/dhcpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog NEWS
%attr(755,root,root) %{_sbindir}/dhcpcd
%dir %{_var}/lib/dhcpc
%{_mandir}/man8/dhcpcd.8*
