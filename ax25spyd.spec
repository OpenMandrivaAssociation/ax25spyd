%define name ax25spyd
%define version 0.23
%define release 9mdk

Name: %{name}
Summary: ax25spyd is a daemon that listens for AX.25 packets from the kernel-AX.25.
Version: %{version}
Release: %{release}
Source: %{name}-%{version}.tar.bz2
Group: System/Servers
Url: http://1409.org/projects/ax25spyd.html
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Requires: libax25_0 >= 0.0.9 
Buildrequires: libncurses-devel ax25-devel

%description
This is ax25spyd (formerly known as monixd), a daemon that listens
for AX.25 packets from the kernel-AX.25. These packets are decoded
(like listen(1)) but not displayed on the screen.

Other programs can connect to ax25spyd via sockets and issue commands.
They will get all heard AX.25-packets in a human-readable format, an
mheard structure, DX-cluster messages or spydata.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%configure

%build

%make

%install
%makeinstall

mkdir -p $RPM_BUILD_ROOT/%_sysconfdir/ax25
mv $RPM_BUILD_ROOT/%{_prefix}/etc/ax25/* $RPM_BUILD_ROOT/%_sysconfdir/ax25/

rm -f $RPM_BUILD_DIR/%{name}-%{version}/examples/Makefile*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*/*
%_sysconfdir/ax25/*
%doc AUTHORS BUGS ChangeLog INSTALL README examples

