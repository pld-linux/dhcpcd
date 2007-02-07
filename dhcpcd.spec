Summary:	DHCP Client Daemon
Summary(de):	DHCPC-D�mon
Summary(es):	Cliente (daemon) DHCP
Summary(fr):	D�mon DHCPC
Summary(pl):	Klient (daemon) DHCP
Summary(pt_BR):	Servidor DHCPC
Summary(tr):	DHCPC sunucu s�re�i (daemon)
Name:		dhcpcd
Version:	3.0.10
Release:	1
License:	GPL v2
Group:		Networking/Daemons
#Source0Download: http://developer.berlios.de/project/filelist.php?group_id=4229
Source0:	http://download.berlios.de/dhcpcd/%{name}-%{version}.tar.bz2
# Source0-md5:	b61c176447e5988294ec8a36cdf00f04
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

%description -l de
dhcpcd ist eine Implementierung des DHCP-Client, spezifiziert in
draft-ietf-dhc-dhcp-09 (wenn -r option nicht angegeben) und RFC1541
(wenn -r option angegeben).

Es bezieht die Host-Infos (IP-Adresse, Netmask, Broadcast-Adresse,
usw.) von einem DHCP-Server und konfiguriert die Netzschnittstelle des
Computers, auf dem es l�uft Es versucht, die Verleihzeit gem�� RFC1541
bzw. draft-ietf-dhc-dhcp-09 zu verl�ngern.

%description -l es
dhcpcd es una implementaci�n del cliente DHCP especificado en
draft-ietf-dhc-dhcp-09 (cuando la opci�n -r no est� especificada) y
RFC1541 (cuando la opci�n -r est� especificada). Captura la
informaci�n del host (direcci�n IP, m�scara de red, direcci�n de
broadcast, etc.) de un servidor DHCP y configura la interface de red
de la m�quina donde est� ejecutando. Tambi�n intenta renovar el tiempo
de alquiler de los direcciones de acuerdo con RFC1541 o
draft-ietf-dhc-dhcp-09.

%description -l fr
dhcpcd est une implantation du client DHCP sp�cifi� dans les
draft-ietf-dhc-dhcp-09 (sans l'option -r) et RFC1541 (avec l'option
- -r).

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
kt�rej jest uruchomiony. Pr�buje r�wnie� od�wie�y� czas przestoju
zgodnie z RFC1541 oraz draft-ietf-dhc-dhcp-09.

%description -l pt_BR
dhcpcd � uma implementa��o do cliente DHCP especificado em
draft-ietf-dhc-dhcp-09 (quando a op��o -r n�o � especificada) e
RFC1541 (quando a op��o -r � especificada). Ele captura a informa��o
do host (endere�o IP, m�scara de rede, endere�o de broadcast, etc.) de
um servidor DHCP e configura a interface de rede da m�quina em que
est� rodando. Ele tamb�m tenta renovar o tempo de aluguel dos
endere�os de acordo com RFC1541 ou draft-ietf-dhc-dhcp-09.

%description -l tr
Makina bilgilerini (IP adresi, a� maskesi, yay�n adresi, vb.) bir DHCP
sunucusundan al�r ve �zerinde �al��t��� makinan�n a� aray�z�n�
ayarlar. Ayr�ca RFC1541 veya draft-ietf-dhc-dhcp-09'a uygun olarak,
kira zaman�n� (lease time) yenilemeye �al���r.

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
install -d $RPM_BUILD_ROOT/var/lib/dhcpc

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	mandir=%{_mandir} \
	sbindir=%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_sbindir}/dhcpcd
%dir %{_var}/lib/dhcpc
%{_mandir}/man8/dhcpcd.8*
