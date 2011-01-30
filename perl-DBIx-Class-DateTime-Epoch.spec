%define upstream_name    DBIx-Class-DateTime-Epoch
%define upstream_version 0.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Automatic inflation/deflation of epoch-based columns to/from DateTime objects
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/DBIx/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(DBICx::TestDatabase)
BuildRequires: perl(DBIx::Class)
BuildRequires: perl(DBIx::Class::DynamicDefault)
BuildRequires: perl(DBIx::Class::TimeStamp)
BuildRequires: perl(DateTime)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Test::More)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module automatically inflates/deflates DateTime objects from/to epoch
values for the specified columns. This module is essentially an extension
to the DBIx::Class::InflateColumn::DateTime manpage so all of the settings,
including 'locale' and 'timezone', are also valid.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*
