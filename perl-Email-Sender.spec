#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Email
%define		pnam	Sender
%include	/usr/lib/rpm/macros.perl
Summary:	Email::Sender - a library for sending email
#Summary(pl.UTF-8):	
Name:		perl-Email-Sender
Version:	1.300020
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	9956cd26dba5a9f803b0d2817df4d873
# generic URL, check or change before uncommenting
#URL:		http://search.cpan.org/dist/Email-Sender/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Email::Abstract) >= 3.006
BuildRequires:	perl(Email::Address)
BuildRequires:	perl(Email::Simple) >= 1.998
BuildRequires:	perl(List::MoreUtils)
BuildRequires:	perl(Module::Runtime)
BuildRequires:	perl(Moo) >= 1.000008
BuildRequires:	perl(Moo::Role)
BuildRequires:	perl(MooX::Types::MooseLike) >= 0.15
BuildRequires:	perl(MooX::Types::MooseLike::Base)
BuildRequires:	perl(Sub::Exporter)
BuildRequires:	perl(Sub::Exporter::Util)
BuildRequires:	perl(Throwable::Error) >= 0.200003
BuildRequires:	perl(Try::Tiny)
BuildRequires:	perl(Capture::Tiny) >= 0.08
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description


# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Email/*.pm
%{perl_vendorlib}/Email/Sender
%{_mandir}/man3/*
