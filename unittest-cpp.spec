%define major	2
%define libname	%mklibname %{name} %{major}
%define devname	%mklibname %{name} -d
%define abi 2.0.0

Name:		unittest-cpp
Version:	2.0.0
Release:	1
Summary:	Lightweight unit testing framework for C++
License:	MIT
Group:		System/Libraries
URL:		https://github.com/unittest-cpp/unittest-cpp
Source0:	https://github.com/unittest-cpp/unittest-cpp/releases/download/v%{version}/%{name}-%{version}.tar.gz
Source1:	%{name}.html
BuildRequires:	gcc-c++
BuildRequires:	glibc-devel

%description
%{name} is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all
very important aspects of %{name}.

#----------------------------------------------------

%package -n	%{libname}
Summary:	Library for %{name}
Group:		System/Libraries

%description -n	%{libname}
%{name} is a lightweight unit testing framework for C++.
Simplicity, portability, speed, and small footprint are all
very important aspects of %{name}.
This package contains library files for %{name}.

%files -n %{libname}
%doc %{name}.html AUTHORS 
%{_libdir}/libUnitTest++.so.%{major}
%{_libdir}/libUnitTest++.so.%{abi}
#----------------------------------------------------

%package -n	%{devname}
Summary:	Object files for development using %{name}
Group:		Development/C
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n	%{devname}
The %{devname} package contains libraries and header files for
developing applications that use %{name}.

%files -n %{devname}
%doc %{name}.html AUTHORS 
%{_includedir}/UnitTest++/
%{_libdir}/libUnitTest++.so
%{_libdir}/pkgconfig/UnitTest++.pc
#----------------------------------------------------

%prep
%setup -q

cp -p %{SOURCE1} .

%build
%configure2_5x --disable-static
%make

%check
make check

%install
%makeinstall_std
