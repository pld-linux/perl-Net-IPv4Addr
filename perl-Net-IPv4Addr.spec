#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Net
%define	pnam	IPv4Addr
Summary:	Net::IPv4Addr - Perl extension for manipulating IPv4 addresses
Summary(pl.UTF-8):   Net::IPv4Addr - rozszerzenie Perla do obróbki adresów IPv4
Name:		perl-Net-IPv4Addr
Version:	0.10
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/F/FR/FRAJULAC/Net-IPv4Addr-%{version}.tar.gz
# Source0-md5:	57aa8e28ebcd4c0c9f15792740e53d3c
URL:		http://search.cpan.org/dist/Net-IPv4Addr/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Net::IPv4Addr provides functions for parsing IPv4 addresses both in
traditional address/netmask format and in the new CIDR format. There
are also methods for calculating the network and broadcast address and
also to see check if a given address is in a specific network.

%description -l pl.UTF-8
Net::IPv4Addr udostępnia funkcje do analizy adresów IPv4 zarówno w
tradycyjnym formacie adres/maska, jak i nowym formacie CIDR. Zawiera
także metody do obliczania adresu sieci i rozgłoszeniowego oraz
sprawdzania, czy dany adres należy do określonej sieci.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/ipv4calc
%{perl_vendorlib}/Net/IPv4Addr.pm
%dir %{perl_vendorlib}/auto/Net/IPv4Addr
%{perl_vendorlib}/auto/Net/IPv4Addr/autosplit.ix
%{_mandir}/man1/ipv4calc.1p*
%{_mandir}/man3/Net::IPv4Addr.3pm*
