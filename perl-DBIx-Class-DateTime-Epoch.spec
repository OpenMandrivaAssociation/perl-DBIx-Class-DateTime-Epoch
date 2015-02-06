%define upstream_name    DBIx-Class-DateTime-Epoch
%define upstream_version 0.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Automatic inflation/deflation of epoch-based columns to/from DateTime objects
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(DBICx::TestDatabase)
BuildRequires:	perl(DBIx::Class)
BuildRequires:	perl(DBIx::Class::DynamicDefault)
BuildRequires:	perl(DBIx::Class::TimeStamp)
BuildRequires:	perl(DateTime)
BuildRequires:	perl(DateTime::Format::SQLite)
BuildRequires:	perl(Module::Find)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Test::More)

BuildArch:	noarch

%description
This module automatically inflates/deflates DateTime objects from/to epoch
values for the specified columns. This module is essentially an extension
to the DBIx::Class::InflateColumn::DateTime manpage so all of the settings,
including 'locale' and 'timezone', are also valid.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.70.0-2mdv2011.0
+ Revision: 656898
- rebuild for updated spec-helper

* Mon Jan 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.70.0-1
+ Revision: 634430
- update to new version 0.07

* Fri Jan 29 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2011.0
+ Revision: 497911
- update to 0.06

* Mon Nov 30 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 471636
- adding missing buildrequires:
- tighten spec file
- import perl-DBIx-Class-DateTime-Epoch


* Sun Nov 29 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
