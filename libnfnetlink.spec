%define major                 0
%define libname               %mklibname nfnetlink %{major}
%define libnamedevel          %mklibname nfnetlink -d
%define libnamedevelold       %mklibname nfnetlink 0-devel
%define libnamestaticdevel    %mklibname nfnetlink -d -s
%define libnamestaticdevelold %mklibname nfnetlink 0-static-devel

Name:           libnfnetlink
Version:        1.0.0
Release:        6
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

%package -n %{libnamestaticdevel}
Summary:        Static development files for %{name}
Group:          System/Libraries
Obsoletes:      %{libnamestaticdevelold} < %{epoch}:%{version}-%{release}
Obsoletes:      %{mklibname -s -d nfnetlink 1} < %{epoch}:%{version}-%{release}
Provides:       nfnetlink-static-devel = %{epoch}:%{version}-%{release}
Requires:       %{libnamedevel} = %{epoch}:%{version}-%{release}

%description -n %{libnamestaticdevel}
This package contains the static development files for %{name}.

%prep
%setup -q

%build
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

%files -n %{libnamestaticdevel}
%{_libdir}/*.a
