%define upstream_name    Crypt-CAST5
%define upstream_version 0.05

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 5

Summary:	Crypt::CAST5 - CAST5 block cipher
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://search.cpan.org/CPAN/authors/id/B/BO/BOBMATH/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

%description
This module provides an implementation of the CAST5 block cipher using
compiled C code for increased speed. CAST5 is also known as CAST-128. It
is a product of the CAST design procedure developed by C. Adams and
S. Tavares. The CAST5 cipher is available royalty-free.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-5mdv2012.0
+ Revision: 765120
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-4
+ Revision: 763617
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.50.0-3
+ Revision: 676770
- rebuild

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-2mdv2011.0
+ Revision: 555708
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 403029
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.05-4mdv2009.0
+ Revision: 256204
- rebuild

* Mon Jan 14 2008 Thierry Vignaud <tv@mandriva.org> 0.05-2mdv2008.1
+ Revision: 151888
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot


* Sun Jul 09 2006 Emmanuel Andry <eandry@mandriva.org> 0.05-1mdv2007.0
- 0.0.5
- %%mkrel

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 0.04-1mdk
- initial Mandriva package

