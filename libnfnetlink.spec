%define major                 0
%define libname               %mklibname nfnetlink %{major}
%define libnamedevel          %mklibname nfnetlink -d
%define libnamedevelold       %mklibname nfnetlink 0-devel

Name:           libnfnetlink
Version:        1.0.1
Release:        1
Epoch:          0
Summary:        Userspace library for handling of netfilter netlink messages
Group:          System/Libraries
License:        GPL
URL:            http://www.netfilter.org/projects/libnfnetlink/index.html
Source0:        http://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-%{version}.tar.bz2
Source1:        http://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-%{version}.tar.bz2.sig

%description
nfnetlink is a netlink(7) based kernel/userspace transport layer. It
provides a unified kernel/userspace interface for the various netfilter
subsystems, such as connection tracking, logging and queueing.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{name} = %{epoch}:%{version}-%{release}
Provides:       nfnetlink = %{epoch}:%{version}-%{release}

%description -n %{libname}
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions. It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%package -n %{libnamedevel}
Summary:        Development files for %{name}
Group:          System/Libraries
Obsoletes:      %{libnamedevelold} < %{epoch}:%{version}-%{release}
Obsoletes:	%{mklibname -d nfnetlink 1} < %{epoch}:%{version}-%{release}
Provides:       nfnetlink-devel = %{epoch}:%{version}-%{release}
Requires:       %{libname} = %{epoch}:%{version}-%{release}

%description -n %{libnamedevel}
This package contains the development files for %{name}.

%prep
%setup -q

%build
autoreconf -fi
%configure2_5x
%make

%install
%makeinstall_std

%check
%make check

rm -f %{buildroot}%{_libdir}/*.la

%files -n %{libname}
%doc README
%{_libdir}/*.so.%{major}*

%files -n %{libnamedevel}
%{_includedir}/libnfnetlink
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnfnetlink.pc


%changelog
* Mon Apr 16 2012 Oden Eriksson <oeriksson@mandriva.com> 0:1.0.0-6
+ Revision: 791223
- various fixes

* Fri Jul 29 2011 Luis Daniel Lucio Quiroz <dlucio@mandriva.org> 0:1.0.0-5
+ Revision: 692318
- trying to make this SPEC compatible with mageia so it will be easier for me

* Mon May 02 2011 Oden Eriksson <oeriksson@mandriva.com> 0:1.0.0-4
+ Revision: 661502
- mass rebuild

* Sun Nov 28 2010 Oden Eriksson <oeriksson@mandriva.com> 0:1.0.0-3mdv2011.0
+ Revision: 602581
- rebuild

  + Luis Daniel Lucio Quiroz <dlucio@mandriva.org>
    - rebuild

* Sat Feb 27 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0:1.0.0-1mdv2010.1
+ Revision: 512395
- update to new version 1.0.0

* Sun Sep 13 2009 Thierry Vignaud <tv@mandriva.org> 0:0.0.41-2mdv2010.0
+ Revision: 438720
- rebuild

* Sun Mar 08 2009 Emmanuel Andry <eandry@mandriva.org> 0:0.0.41-1mdv2009.1
+ Revision: 352828
- New version 0.0.41
- fix macros syntax

* Mon Jan 19 2009 Jérôme Soyer <saispo@mandriva.org> 0:0.0.40-1mdv2009.1
+ Revision: 331192
- New upstream release

* Sat Aug 16 2008 Funda Wang <fwang@mandriva.org> 0:0.0.39-2mdv2009.0
+ Revision: 272606
- obsoletes old devel libs

* Sun Jul 27 2008 David Walluck <walluck@mandriva.org> 0:0.0.39-1mdv2009.0
+ Revision: 250486
- 0.0.39

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Sun Apr 20 2008 David Walluck <walluck@mandriva.org> 0:0.0.33-1mdv2009.0
+ Revision: 195978
- 0.0.33

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Oct 25 2007 David Walluck <walluck@mandriva.org> 0:0.0.30-2mdv2008.1
+ Revision: 101969
- rebuild

* Tue Sep 04 2007 David Walluck <walluck@mandriva.org> 0:0.0.30-1mdv2008.0
+ Revision: 79233
- 0.0.30
- new lib policy

* Thu May 24 2007 David Walluck <walluck@mandriva.org> 0:0.0.25-3mdv2008.0
+ Revision: 30602
- really fix major

* Thu May 24 2007 David Walluck <walluck@mandriva.org> 0:0.0.25-2mdv2008.0
+ Revision: 30564
- fix lib major version

* Wed May 23 2007 David Walluck <walluck@mandriva.org> 0:0.0.25-1mdv2008.0
+ Revision: 30373
- 0.0.25

* Sun Apr 22 2007 David Walluck <walluck@mandriva.org> 0:0.0.16-3mdv2008.0
+ Revision: 16713
- include sig file


* Fri Sep 15 2006 David Walluck <walluck@mandriva.org> 0:0.0.16-1mdv2007.0
- release

