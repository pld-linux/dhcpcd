Summary:	DHCP Client Daemon
Summary(de.UTF-8):	DHCPC-Dämon
Summary(es.UTF-8):	Cliente (daemon) DHCP
Summary(fr.UTF-8):	Démon DHCPC
Summary(pl.UTF-8):	Klient (daemon) DHCP
Summary(pt_BR.UTF-8):	Servidor DHCPC
Summary(tr.UTF-8):	DHCPC sunucu süreçi (daemon)
Name:		dhcpcd
Version:	3.1.8
Release:	2
License:	GPL v2
Group:		Networking/Daemons
#Source0Download: http://developer.berlios.de/project/filelist.php?group_id=4229
Source0:	http://download.berlios.de/dhcpcd/%{name}-%{version}.tar.bz2
# Source0-md5:	6332c695e28100acbb84730e7ff7f6e9
Patch0:		%{name}-ntp-path.patch
URL:		http://developer.berlios.de/projects/dhcpcd/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir	/sbin

%description
dhcpcd is an implementation of the DHCP client specified in
draft-ietf-dhc-dhcp-09 (when -r option is not specified) and RFC1541
(when -r option is specified).

It gets the host information (IP address, netmask, broadcast address,
etc.) from a DHCP server and configures the network interface of the
machine on which it is running. It also tries to renew the lease time
according to RFC1541 or draft-ietf-dhc-dhcp-09.

%description -l de.UTF-8
dhcpcd ist eine Implementierung des DHCP-Client, spezifiziert in
draft-ietf-dhc-dhcp-09 (wenn -r option nicht angegeben) und RFC1541
(wenn -r option angegeben).

Es bezieht die Host-Infos (IP-Adresse, Netmask, Broadcast-Adresse,
usw.) von einem DHCP-Server und konfiguriert die Netzschnittstelle des
Computers, auf dem es läuft Es versucht, die Verleihzeit gemäß RFC1541
bzw. draft-ietf-dhc-dhcp-09 zu verlängern.

%description -l es.UTF-8
dhcpcd es una implementación del cliente DHCP especificado en
draft-ietf-dhc-dhcp-09 (cuando la opción -r no está especificada) y
RFC1541 (cuando la opción -r está especificada). Captura la
información del host (dirección IP, máscara de red, dirección de
broadcast, etc.) de un servidor DHCP y configura la interface de red
de la máquina donde esté ejecutando. También intenta renovar el tiempo
de alquiler de los direcciones de acuerdo con RFC1541 o
draft-ietf-dhc-dhcp-09.

%description -l fr.UTF-8
dhcpcd est une implantation du client DHCP spécifié dans les
draft-ietf-dhc-dhcp-09 (sans l'option -r) et RFC1541 (avec l'option
- -r).

Il obtient l'information sur l'hôte (adresse IP, masque réseau,
adresse de diffusion, etc.) à partir d'un serveur DHCP et configure
l'interface réseau de la machine sur laquelle il tourne. Il essaie
aussi de renouveler le « lease time » selon les RFC1541 ou
draft-ietf-dhc-dhcp-09.

%description -l pl.UTF-8
dhcpd jest implementacja klienta DHCP, opisaną w
draft-ietf-dhc-dhcp-09 (kiedy nie podaje się opcji -r) oraz RFC1544
(kiedy podaje się opcję -r).

Pobiera on informację o komputerze (adres IP, maska sieci, adres
rozgłoszeniowy itd.) i konfiguruje interfejs sieciowy maszyny, na
której jest uruchomiony. Próbuje również odświeżyć czas przestoju
zgodnie z RFC1541 oraz draft-ietf-dhc-dhcp-09.

%description -l pt_BR.UTF-8
dhcpcd é uma implementação do cliente DHCP especificado em
draft-ietf-dhc-dhcp-09 (quando a opção -r não é especificada) e
RFC1541 (quando a opção -r é especificada). Ele captura a informação
do host (endereço IP, máscara de rede, endereço de broadcast, etc.) de
um servidor DHCP e configura a interface de rede da máquina em que
está rodando. Ele também tenta renovar o tempo de aluguel dos
endereços de acordo com RFC1541 ou draft-ietf-dhc-dhcp-09.

%description -l tr.UTF-8
Makina bilgilerini (IP adresi, ağ maskesi, yayın adresi, vb.) bir DHCP
sunucusundan alır ve üzerinde çalıştığı makinanın ağ arayüzünü
ayarlar. Ayrıca RFC1541 veya draft-ietf-dhc-dhcp-09'a uygun olarak,
kira zamanını (lease time) yenilemeye çalışır.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmcflags} %{rpmldflags}" \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},/var/lib/dhcpc}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}

# do not put executable bit here when installing
cp -a dhcpcd.sh $RPM_BUILD_ROOT%{_sysconfdir}/dhcpcd.sh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dhcpcd.sh
%attr(755,root,root) %{_sbindir}/dhcpcd
%dir %{_var}/lib/dhcpc
%{_mandir}/man8/dhcpcd.8*
