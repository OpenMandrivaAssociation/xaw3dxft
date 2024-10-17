%define name	xaw3dxft
%define version	1.3
%define release	2

%define major 6
%define libname %mklibname %{name} %{major}
%define develname %mklibname %{name} -d

Summary:	An extended version of Xaw3d
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{release}
Group:		System/Libraries
BuildRequires:	X11-devel
BuildRequires:	libxp-devel
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	imake
BuildRequires:	gccmakedep
Source0:	http://downloads.sourceforge.net/project/sf-xpaint/sf-xpaint/%{name}-%{version}/%{name}-%{version}.tar.bz2
Url:		https://sourceforge.net/projects/sf-xpaint/
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
%setup -q -n Xaw3dxft

%build
xmkmf -a

# fix compiler flags
perl -pi -e 's|(CDEBUGFLAGS =.*)|CDEBUGFLAGS = %{optflags}|g' Makefile
perl -pi -e 's|(CXXDEBUGFLAGS =.*)|CXXDEBUGFLAGS = %{optflags}|g' Makefile

export SHLIBGLOBALSFLAGS="%{ldflags}"
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/*.so.%{major}*

%files -n %{develname}
%defattr(-,root,root)
%doc README*
%{_libdir}/*.so
%{_includedir}/X11/Xaw3dxft


%changelog
* Tue Nov 09 2010 Jani Välimaa <wally@mandriva.org> 1.3-1mdv2011.0
+ Revision: 595491
- new version 1.3
- drop now unneeded patch

* Sun Oct 03 2010 Jani Välimaa <wally@mandriva.org> 1.2-1.1mdv2011.0
+ Revision: 582654
- add patch to sync sources with xaw3dxft shipped with xpaint 2.9.6.2

* Tue Sep 07 2010 Jani Välimaa <wally@mandriva.org> 1.2-1mdv2011.0
+ Revision: 576584
- add missing BR
- new version 1.2
- use LDFLAGS

* Sun Mar 28 2010 Jani Välimaa <wally@mandriva.org> 1.1-1mdv2010.1
+ Revision: 528551
- import xaw3dxft


