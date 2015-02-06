Name:		ax25spyd
Summary:	Daemon that listens for AX.25 packets from the kernel-AX.25
Version:	0.23
Release:	16
Source:		http://linkt.de/ax25spyd/%{name}-%{version}.tar.bz2
# From Debian: fixes build - AdamW 2008/01
Patch0:		ax25spyd-0.23-build.patch
Patch1:		ax25spyd-0.23-str_fmt.patch
Group:		System/Servers
URL:		http://linkt.de/ax25spyd/
License:	GPLv2+
BuildRequires:	pkgconfig(ncurses)
BuildRequires:	ax25-devel

%description
This is ax25spyd (formerly known as monixd), a daemon that listens
for AX.25 packets from the kernel-AX.25. These packets are decoded
(like listen(1)) but not displayed on the screen.

Other programs can connect to ax25spyd via sockets and issue commands.
They will get all heard AX.25-packets in a human-readable format, an
mheard structure, DX-cluster messages or spydata.

%prep
%setup -q
%patch0 -p1 -b .build
%patch1 -p0 -b .strfmt
%build
%configure2_5x
%make

%install
%makeinstall_std

mkdir -p %{buildroot}/%_sysconfdir/ax25
mv %{buildroot}/%{_prefix}/etc/ax25/* %{buildroot}/%{_sysconfdir}/ax25/

#doc cleaning
rm -f examples/Makefile*

%files
%defattr(-,root,root)
%{_bindir}/*
%{_sbindir}/*
%{_mandir}/*/*
%{_sysconfdir}/ax25/*
%doc AUTHORS BUGS ChangeLog INSTALL README examples



%changelog
* Tue Dec 21 2010 Jani Välimaa <wally@mandriva.org> 0.23-14mdv2011.0
+ Revision: 623706
- add str fmt patch
- fix url and source tags
- clean .spec a bit

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.23-12mdv2009.0
+ Revision: 243107
- rebuild

* Fri Feb 01 2008 Adam Williamson <awilliamson@mandriva.org> 0.23-10mdv2008.1
+ Revision: 160956
- drop explicit requires on libax25
- rebuild for new era
- new license policy
- spec clean
- add build.patch (from Debian, fixes build)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - use %%mkrel
    - fix summary-ended-with-dot
    - import ax25spyd


* Thu Aug 05 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.23-9mdk
- rebuild

* Thu Jun 03 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.23-8mdk
- rebuild

* Sat Apr 26 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.23-7mdk
- adjust buildrequires

* Thu Jan 30 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.23-6mdk
- rebuild

* Fri May 31 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.23-5mdk
- fix requires on ax25-tools

* Tue May 21 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.23-4mdk
- fix group
- fix buildrequires
- remove zero-length doc file

* Sat Dec 08 2001 Laurent Grawet <laurent.grawet@ibelgique.com> 0.23-3mdk
- corrected "Requires" and "Group"

* Thu Jul 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.23-2mdk
- bm
- macros

* Tue Jun 27 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.23-1mdk
- new in contribs
