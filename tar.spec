#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x3602B07F55D0C732 (gray@gnu.org)
#
Name     : tar
Version  : 1.29
Release  : 17
URL      : http://ftp.gnu.org/gnu/tar/tar-1.29.tar.xz
Source0  : http://ftp.gnu.org/gnu/tar/tar-1.29.tar.xz
Source99 : http://ftp.gnu.org/gnu/tar/tar-1.29.tar.xz.asc
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.3 GPL-3.0 GPL-3.0+
Requires: tar-bin
Requires: tar-doc
Requires: tar-locales
BuildRequires : acl-dev
BuildRequires : bison
Patch1: CVE-2016-6321.patch
Patch2: timestamp.patch

%description
See the end of file for copying conditions.
* Introduction
Please glance through *all* sections of this
'ABOUT-NLS' and 'INSTALL' if you are not familiar with them already.

%package bin
Summary: bin components for the tar package.
Group: Binaries

%description bin
bin components for the tar package.


%package doc
Summary: doc components for the tar package.
Group: Documentation

%description doc
doc components for the tar package.


%package locales
Summary: locales components for the tar package.
Group: Default

%description locales
locales components for the tar package.


%prep
%setup -q -n tar-1.29
%patch1 -p1
%patch2 -p1

%build
export LANG=C
export SOURCE_DATE_EPOCH=1484402487
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1484402487
rm -rf %{buildroot}
%make_install
%find_lang tar

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/tar
/usr/libexec/rmt

%files doc
%defattr(-,root,root,-)
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files locales -f tar.lang
%defattr(-,root,root,-)

