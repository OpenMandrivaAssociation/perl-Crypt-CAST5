%define real_name Crypt-CAST5

Summary:	Crypt::CAST5 - CAST5 block cipher
Name:		perl-%{real_name}
Version:	0.05
Release:	%mkrel 2
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BO/BOBMATH/%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module provides an implementation of the CAST5 block cipher using
compiled C code for increased speed. CAST5 is also known as CAST-128. It
is a product of the CAST design procedure developed by C. Adams and
S. Tavares. The CAST5 cipher is available royalty-free.

%prep
%setup -q -n %{real_name}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%dir %{perl_vendorlib}/*/auto/Crypt/CAST5
%{perl_vendorlib}/*/Crypt/CAST5.pm
%{perl_vendorlib}/*/auto/Crypt/CAST5/CAST5.so
%{_mandir}/*/*

