Name:		ax25spyd
Summary:	Daemon that listens for AX.25 packets from the kernel-AX.25
Version:	0.23
Release:	%mkrel 14
Source:		%{name}-%{version}.tar.bz2
# From Debian: fixes build - AdamW 2008/01
Patch0:		ax25spyd-0.23-build.patch
Group:		System/Servers
URL:		http://1409.org/projects/ax25spyd.html
BuildRoot:	%{_tmppath}/%{name}-buildroot
License:	GPLv2+
BuildRequires:	libncurses-devel
BuildRequires:	ax25-devel

%description
This is ax25spyd (formerly known as monixd), a daemon that listens
for AX.25 packets from the kernel-AX.25. These packets are decoded
(like listen(1)) but not displayed on the screen.

Other programs can connect to ax25spyd via sockets and issue commands.
They will get all heard AX.25-packets in a human-readable format, an
mheard structure, DX-cluster messages or spydata.

%prep
rm -rf %{buildroot}
%setup -q
%patch0 -p1 -b .build
%configure

%build
%make

%install
%makeinstall

mkdir -p %{buildroot}/%_sysconfdir/ax25
mv %{buildroot}/%{_prefix}/etc/ax25/* %{buildroot}/%_sysconfdir/ax25/

rm -f $RPM_BUILD_DIR/%{name}-%{version}/examples/Makefile*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*/*
%{_sysconfdir}/ax25/*
%doc AUTHORS BUGS ChangeLog INSTALL README examples

