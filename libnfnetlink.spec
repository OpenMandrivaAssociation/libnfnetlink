# libnfnetlink is used by iptables, iptables is used by systemd,
# libsystemd is used by wine
%ifarch %{x86_64}
%bcond_without compat32
%else
%bcond_with compat32
%endif

%define major	0
%define libname	%mklibname nfnetlink %{major}
%define devname	%mklibname nfnetlink -d
%define lib32name libnfnetlink%{major}
%define dev32name libnfnetlink-devel

Summary:        Userspace library for handling of netfilter netlink messages
Name:           libnfnetlink
Version:	1.0.2
Release:	2
Group:          System/Libraries
License:        GPLv2
Url:            https://www.netfilter.org/projects/libnfnetlink/index.html
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

%if %{with compat32}
%package -n %{lib32name}
Summary:        Main library for %{name} (32-bit)
Group:          System/Libraries
BuildRequires:       libc6

%description -n %{lib32name}
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions. It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%package -n %{dev32name}
Summary:        Development files for %{name} (32-bit)
Group:          System/Libraries
Requires:       %{devname} = %{EVRD}
Requires:       %{lib32name} = %{version}-%{release}

%description -n %{dev32name}
This package contains the development files for %{name}.
%endif

%prep
%autosetup -p1

export CONFIGURE_TOP="$(pwd)"

%if %{with compat32}
mkdir build32
cd build32
%configure32
cd ..
%endif

%ifarch %{arm} %{armx}
# Something causes the final link to fail with ld pretending to
# not understand emulation aarch64linux
export CC=gcc
export CXX=g++
%endif
mkdir build
cd build
%configure

%build
%if %{with compat32}
%make_build -C build32
%endif
%make_build -C build

%install
%if %{with compat32}
%make_install -C build32
%endif
%make_install -C build

%check
%if %{with compat32}
%make_build check -C build32
%endif
%make_build check -C build

%files -n %{libname}
%{_libdir}/libnfnetlink.so.%{major}*

%files -n %{devname}
%doc README
%{_includedir}/libnfnetlink
%{_libdir}/*.so
%{_libdir}/pkgconfig/libnfnetlink.pc

%if %{with compat32}
%files -n %{lib32name}
%{_prefix}/lib/libnfnetlink.so.%{major}*

%files -n %{dev32name}
%{_prefix}/lib/*.so
%{_prefix}/lib/pkgconfig/libnfnetlink.pc
%endif
