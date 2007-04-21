%define lib_major       1
%define lib_name_orig   %mklibname nfnetlink
%define lib_name        %{lib_name_orig}%{lib_major}

Name:           libnfnetlink
Version:        0.0.16
Release:        %mkrel 3
Epoch:          0
Summary:        Userspace library for handling of netfilter netlink messages
Group:          System/Libraries
License:        GPL
URL:            http://www.netfilter.org/projects/%{name}/index.html
Source0:        http://ftp.netfilter.org/pub/%{name}/%{name}-%{version}.tar.bz2
Source1:        http://ftp.netfilter.org/pub/%{name}/%{name}-%{version}.tar.bz2.sig
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root

%description
nfnetlink is a netlink(7) based kernel/userspace transport layer. It
provides a unified kernel/userspace interface for the various netfilter
subsystems, such as connection tracking, logging and queueing.

%package -n %{lib_name}
Summary:        Main library for %{name}
Group:          System/Libraries
Provides:       %{lib_name_orig} = %{epoch}:%{version}-%{release}
Provides:       %{name} = %{epoch}:%{version}-%{release}

%description -n %{lib_name}
libnfnetlink is a userspace library that provides some low-level
nfnetlink handling functions. It is used as a foundation for other, netfilter
subsystem specific libraries such as libnfnetlink_conntrack, libnfnetlink_log
and libnfnetlink_queue.

%package -n %{lib_name}-devel
Summary:        Development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name} = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig}-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name}-devel
This package contains the development files for %{name}.

%package -n %{lib_name}-static-devel
Summary:        Static development files for %{name}
Group:          System/Libraries
Requires:       %{lib_name}-devel = %{epoch}:%{version}-%{release}
Provides:       %{lib_name_orig}-static-devel = %{epoch}:%{version}-%{release}
Provides:       %{name}-static-devel = %{epoch}:%{version}-%{release}
Provides:       lib%{name}-static-devel = %{epoch}:%{version}-%{release}

%description -n %{lib_name}-static-devel
This package contains the static development files for %{name}.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%{__rm} -rf %{buildroot}
%makeinstall

%check
%make check

%clean
%{__rm} -rf %{buildroot}

%post -n %{lib_name} -p /sbin/ldconfig

%postun -n %{lib_name} -p /sbin/ldconfig

%files -n %{lib_name}
%defattr(-,root,root,-)
%doc README
%{_libdir}/*.so.*

%files -n %{lib_name}-devel
%defattr(-,root,root,-)
%{_includedir}/%{name}
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_libdir}/*.la

%files -n %{lib_name}-static-devel
%defattr(-,root,root,-)
%{_libdir}/*.a


