%define modname	Crypt-CAST5
%define modver	0.05

Summary:	Crypt::CAST5 - CAST5 block cipher
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BO/BOBMATH/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel

%description
This module provides an implementation of the CAST5 block cipher using
compiled C code for increased speed. CAST5 is also known as CAST-128. It
is a product of the CAST design procedure developed by C. Adams and
S. Tavares. The CAST5 cipher is available royalty-free.

%prep
%setup -qn %{modname}-%{modver}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%dir %{perl_vendorlib}/*/auto/Crypt/CAST5
%{perl_vendorlib}/*/Crypt/CAST5.pm
%{perl_vendorlib}/*/auto/Crypt/CAST5/CAST5.so
%{_mandir}/man3/*

