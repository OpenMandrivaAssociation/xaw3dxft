%define name	xaw3dxft
%define version	1.1
%define release	1

%define major 6
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	An extended version of Xaw3d
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		System/Libraries
BuildRequires:	X11-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imake
BuildRequires:	gccmakedep
Source0:	http://downloads.sourceforge.net/project/sf-xpaint/sf-xpaint/%{name}-%{version}/%{name}-%{version}.tar.bz2
Url:		http://sourceforge.net/projects/sf-xpaint/
License:	MIT
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
An extended version of Xaw3d with support for UTF8 input
and UTF8 encoding of text, and rendering text with the Freetype 
library and Truetype fonts.

It should be mostly compatible with the original xaw3d library,
except for font management: everything using the old X11 core
font routines should be replaced by their freetype equivalents.

%package -n	%{libname}
Summary:	An extended version of Xaw3d
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{libname}
An extended version of Xaw3d with support for UTF8 input and
UTF8 encoding of text, and rendering text with the Freetype
library and Truetype fonts.

It should be mostly compatible with the original Xaw3d library,
except for font management: everything using the old X11 core
font routines should be replaced by their freetype equivalents.

%package -n	%{develname}
Summary:	Header files and shared libraries for development using Xaw3dxft
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %version-%release

%description -n	%{develname}
An extended version of Xaw3d with support for UTF8 input and
UTF8 encoding of text, and rendering text with the Freetype
library and Truetype fonts.

It should be mostly compatible with the original Xaw3d library,
except for font management: everything using the old X11 core
font routines should be replaced by their freetype equivalents.

You should install Xaw3dxft-devel if you are going to develop
applications using the Xaw3dxft widget set.

%prep
%setup -q -c
 
%build
cd xaw3dxft-1.1
xmkmf -a

# fix compiler flags
perl -pi -e 's|(CDEBUGFLAGS =.*)|CDEBUGFLAGS = %{optflags}|g' Makefile
perl -pi -e 's|(CXXDEBUGFLAGS =.*)|CXXDEBUGFLAGS = %{optflags}|g' Makefile

# fix overlinking
sed -i -e 's|$(SMLIB)||g' Makefile
sed -i -e 's|$(ICELIB)||g' Makefile
sed -i -e 's|$(XPMLIB)||g' Makefile
sed -i -e 's|$(XPLIB)||g' Makefile

%make

%install
rm -rf %{buildroot}
cd xaw3dxft-1.1
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc xaw3dxft-1.1/README*
%{_libdir}/*.so
%{_includedir}/X11/Xaw3dxft