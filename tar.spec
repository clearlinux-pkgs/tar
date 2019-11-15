#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3602B07F55D0C732 (gray@gnu.org)
#
Name     : tar
Version  : 1.32
Release  : 31
URL      : https://mirrors.kernel.org/gnu/tar/tar-1.32.tar.xz
Source0  : https://mirrors.kernel.org/gnu/tar/tar-1.32.tar.xz
Source1 : https://mirrors.kernel.org/gnu/tar/tar-1.32.tar.xz.sig
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+
Requires: tar-bin = %{version}-%{release}
Requires: tar-info = %{version}-%{release}
Requires: tar-libexec = %{version}-%{release}
Requires: tar-license = %{version}-%{release}
Requires: tar-locales = %{version}-%{release}
Requires: tar-man = %{version}-%{release}
Requires: xz-bin
Requires: zstd-bin
BuildRequires : acl-dev
BuildRequires : automake
BuildRequires : automake-dev
BuildRequires : bison
BuildRequires : gettext-bin
BuildRequires : glibc-locale
BuildRequires : glibc-staticdev
BuildRequires : libtool
BuildRequires : libtool-dev
BuildRequires : m4
BuildRequires : pkg-config-dev
Patch1: timestamp.patch
Patch2: blocking.patch

%description
See the end of file for copying conditions.
* Introduction
Please glance through *all* sections of this
'ABOUT-NLS' and 'INSTALL' if you are not familiar with them already.

%package bin
Summary: bin components for the tar package.
Group: Binaries
Requires: tar-libexec = %{version}-%{release}
Requires: tar-license = %{version}-%{release}

%description bin
bin components for the tar package.


%package info
Summary: info components for the tar package.
Group: Default

%description info
info components for the tar package.


%package libexec
Summary: libexec components for the tar package.
Group: Default
Requires: tar-license = %{version}-%{release}

%description libexec
libexec components for the tar package.


%package license
Summary: license components for the tar package.
Group: Default

%description license
license components for the tar package.


%package locales
Summary: locales components for the tar package.
Group: Default

%description locales
locales components for the tar package.


%package man
Summary: man components for the tar package.
Group: Default

%description man
man components for the tar package.


%prep
%setup -q -n tar-1.32
cd %{_builddir}/tar-1.32
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1573791177
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fno-lto -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static LDFLAGS=-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1573791177
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/tar
cp %{_builddir}/tar-1.32/COPYING %{buildroot}/usr/share/package-licenses/tar/8624bcdae55baeef00cd11d5dfcfa60f68710a02
%make_install
%find_lang tar

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tar

%files info
%defattr(0644,root,root,0755)
/usr/share/info/tar.info
/usr/share/info/tar.info-1
/usr/share/info/tar.info-2

%files libexec
%defattr(-,root,root,-)
/usr/libexec/rmt

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/tar/8624bcdae55baeef00cd11d5dfcfa60f68710a02

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/tar.1
/usr/share/man/man8/rmt.8

%files locales -f tar.lang
%defattr(-,root,root,-)

