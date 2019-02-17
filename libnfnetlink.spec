%ifarch %{arm} %{armx}
# Libtool somehow messes things up, resulting in gold screaming
# /usr/bin/ld: error: unrecognized emulation aarch64linux
# Even on aarch64, with ld definitely supporting the right target
%global optflags %{optflags} -fuse-ld=bfd
%endif

%define major	0
%define libname	%mklibname nfnetlink %{major}
%define devname	%mklibname nfnetlink -d

Summary:        Userspace library for handling of netfilter netlink messages
Name:           libnfnetlink
Version:        1.0.1
Release:        17
Group:          System/Libraries
License:        GPLv2
Url:            http://www.netfilter.org/projects/libnfnetlink/index.html
Source0:        http://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-%{version}.tar.bz2
Source1:        http://www.netfilter.org/projects/libnfnetlink/files/libnfnetlink-%{version}.tar.bz2.sig

%description
nfnetlink is a netlink(7) based kernel/userspace transport layer. It
provides a unified kernel/userspace interface for the various netfilter
subsystems, such as connection tracking, logging and queueing.

%package -n %{libname}
Summary:        Main library for %{name}
Group:          System/Libraries

%description -n %{libname}
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions. It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%package -n %{devname}
Summary:        Development files for %{name}
Group:          System/Libraries
Provides:       nfnetlink-devel = %{version}-%{release}
Requires:       %{libname} = %{version}-%{release}

%description -n %{devname}
This package contains the development files for %{name}.

%prep
%setup -q
libtoolize --force
autoreconf -fi

%build
%configure
%make

%install
%makeinstall_std

%check
%make check

%files -n %{libname}
%{_libdir}/libnfnetlink.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/libnfnetlink
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnfnetlink.pc

