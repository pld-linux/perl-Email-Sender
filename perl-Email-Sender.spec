# TODO:
#	- Obsolete perl-Email-Send?
#
# Conditional build:
%bcond_without	tests		# do not perform "make test"

%define		pdir	Email
%define		pnam	Sender
%include	/usr/lib/rpm/macros.perl
Summary:	Email::Sender - a library for sending email
Name:		perl-Email-Sender
Version:	1.300030
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Email/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3a0c24feba2e8ba89c30f9d95beae74b
URL:		https://github.com/rjbs/Email-Sender
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Capture::Tiny) >= 0.08
BuildRequires:	perl(Email::Abstract) >= 3.006
BuildRequires:	perl(Email::Simple) >= 1.998
BuildRequires:	perl(Moo) >= 1.000008
BuildRequires:	perl(MooX::Types::MooseLike) >= 0.15
BuildRequires:	perl(MooX::Types::MooseLike::Base)
BuildRequires:	perl(Throwable::Error) >= 0.200003
BuildRequires:	perl-Email-Address
BuildRequires:	perl-List-MoreUtils
BuildRequires:	perl-Module-Runtime
BuildRequires:	perl-Moo
BuildRequires:	perl-Sub-Exporter
BuildRequires:	perl-Try-Tiny
%endif
Requires:	perl-Throwable
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Email::Sender replaces the old and sometimes problematic Email::Send
library, which did a decent job at handling very simple email sending
tasks, but was not suitable for serious use, for a variety of reasons.

Most users will be able to use Email::Sender::Simple to send mail.
Users with more specific needs should look at the available
Email::Sender::Transport classes.

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
