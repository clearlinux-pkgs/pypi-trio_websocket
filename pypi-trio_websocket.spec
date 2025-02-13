#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-trio_websocket
Version  : 0.11.1
Release  : 18
URL      : https://files.pythonhosted.org/packages/dd/36/abad2385853077424a11b818d9fd8350d249d9e31d583cb9c11cd4c85eda/trio-websocket-0.11.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/dd/36/abad2385853077424a11b818d9fd8350d249d9e31d583cb9c11cd4c85eda/trio-websocket-0.11.1.tar.gz
Summary  : WebSocket library for Trio
Group    : Development/Tools
License  : MIT
Requires: pypi-trio_websocket-license = %{version}-%{release}
Requires: pypi-trio_websocket-python = %{version}-%{release}
Requires: pypi-trio_websocket-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(trio)
BuildRequires : pypi(wsproto)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Trio WebSocket
This library implements both server and client aspects of the [the WebSocket
protocol](https://tools.ietf.org/html/rfc6455), striving for safety,
correctness, and ergonomics. It is based on the [wsproto
project](https://wsproto.readthedocs.io/en/latest/), which is a
[Sans-IO](https://sans-io.readthedocs.io/) state machine that implements the
majority of the WebSocket protocol, including framing, codecs, and events. This
library handles I/O using [the Trio
framework](https://trio.readthedocs.io/en/latest/). This library passes the
[Autobahn Test Suite](https://github.com/crossbario/autobahn-testsuite).

%package license
Summary: license components for the pypi-trio_websocket package.
Group: Default

%description license
license components for the pypi-trio_websocket package.


%package python
Summary: python components for the pypi-trio_websocket package.
Group: Default
Requires: pypi-trio_websocket-python3 = %{version}-%{release}

%description python
python components for the pypi-trio_websocket package.


%package python3
Summary: python3 components for the pypi-trio_websocket package.
Group: Default
Requires: python3-core
Provides: pypi(trio_websocket)
Requires: pypi(trio)
Requires: pypi(wsproto)

%description python3
python3 components for the pypi-trio_websocket package.


%prep
%setup -q -n trio-websocket-0.11.1
cd %{_builddir}/trio-websocket-0.11.1
pushd ..
cp -a trio-websocket-0.11.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1695826447
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-trio_websocket
cp %{_builddir}/trio-websocket-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-trio_websocket/694bd0afdd8360a159776129986bc45ad2f3c374 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-trio_websocket/694bd0afdd8360a159776129986bc45ad2f3c374

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
