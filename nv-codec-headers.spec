#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
%define keepstatic 1
Name     : nv-codec-headers
Version  : 11.0.10.2
Release  : 301
URL      : file:///aot/build/clearlinux/packages/nv-codec-headers/nv-codec-headers-v11.0.10.2.tar.gz
Source0  : file:///aot/build/clearlinux/packages/nv-codec-headers/nv-codec-headers-v11.0.10.2.tar.gz
Summary  : FFmpeg version of Nvidia Codec SDK headers
Group    : Development/Tools
License  : GPL-2.0
Requires: pkg-config
BuildRequires : findutils
BuildRequires : pkg-config
BuildRequires : pkg-config-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
# Suppress generation of debuginfo
%global debug_package %{nil}

%description
FFmpeg version of headers required to interface with Nvidias codec APIs.
Corresponds to Video Codec SDK version 11.0.10.

%package dev
Summary: dev components for the nv-codec-headers package.
Group: Development
Provides: nv-codec-headers-devel = %{version}-%{release}
Requires: nv-codec-headers = %{version}-%{release}

%description dev
dev components for the nv-codec-headers package.


%prep
%setup -q -n nv-codec-headers
cd %{_builddir}/nv-codec-headers

%build
unset http_proxy
unset https_proxy
unset no_proxy
export SSL_CERT_FILE=/var/cache/ca-certs/anchors/ca-certificates.crt
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1623566568
unset LD_AS_NEEDED
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=16 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=16 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=16 "
make  %{?_smp_mflags}  V=1 VERBOSE=1  V=1 VERBOSE=1


%install
export SOURCE_DATE_EPOCH=1623566568
rm -rf %{buildroot}
## install_macro start
make install V=1 VERBOSE=1 DESTDIR=%{buildroot} LIBDIR=lib64
## install_macro end

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/ffnvcodec/dynlink_cuda.h
/usr/include/ffnvcodec/dynlink_cuviddec.h
/usr/include/ffnvcodec/dynlink_loader.h
/usr/include/ffnvcodec/dynlink_nvcuvid.h
/usr/include/ffnvcodec/nvEncodeAPI.h
/usr/lib64/pkgconfig/ffnvcodec.pc
