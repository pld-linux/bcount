%define		_test	test2
Summary:	Bytes counter
Summary(pl):	Licznik bajtów
Name:		bcount
Version:	1.0
Release:	0.%{_test}.2
License:	GPL
Group:		Networking/Utilities
Source0:	http://www.deth.org.pl/~alex/bcount/%{name}-%{version}%{_test}.tar.gz
# Source0-md5:	af92076cb4dbb870b991b677d0ad3bc2
Patch0:		%{name}-ncurses.patch
URL:		http://www.deth.org.pl/~alex/bcount/
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bytes Counter displays detailed information about the number of bytes
and packets that have been transferred over a network interface.

%description -l pl
Bcount jest licznikiem pokazuj±cym informacjê o bajtach i pakietach
przechodz±cych przez interfejs sieciowy.

%prep
%setup -q -n %{name}-%{version}%{_test}
%patch0 -p1

%build
%configure \
	 \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sbindir},%{_var}/log}
install bcount $RPM_BUILD_ROOT%{_sbindir}

:> $RPM_BUILD_ROOT%{_var}/log/bcount.log

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO README.protocol
%doc README.log README.ethx README.fuckyou
%attr(755,root,root) %{_sbindir}/*
%attr(640,root,root) %ghost %{_var}/log/bcount.log
