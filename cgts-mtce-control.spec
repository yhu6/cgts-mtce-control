#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : cgts-mtce-control
Version  : 6a5e10492cf09b47463cd38d806c36386a459718
Release  : 10
URL      : https://github.com/openstack/stx-metal/archive/6a5e10492cf09b47463cd38d806c36386a459718.tar.gz
Source0  : https://github.com/openstack/stx-metal/archive/6a5e10492cf09b47463cd38d806c36386a459718.tar.gz
Summary  : Titanium Cloud Platform Common Node Maintenance Package
Group    : Development/Tools
License  : Apache-2.0
Requires: cgts-mtce-control-data
Requires: /bin/systemctl
Requires: bash
Requires: lighttpd
Requires: qemu-kvm-ev
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : systemd
BuildRequires : systemd-devel
BuildRequires : tox
BuildRequires : virtualenv
Patch1: 0001-add-Makefile-for-cgts-mtce-control-1.0.patch

%description
agent/client daemons as well as the hardware and process monitor
             daemons, hardware watchdog process, resource and file system daemons
             as well as initialization and support files for each.

%package data
Summary: data components for the cgts-mtce-control package.
Group: Data

%description data
data components for the cgts-mtce-control package.


%prep
%setup -q -n stx-metal-6a5e10492cf09b47463cd38d806c36386a459718
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1539241905
pushd mtce-control/cgts-mtce-control-1.0
make  %{?_smp_mflags} default
popd

%install
export SOURCE_DATE_EPOCH=1539241905
rm -rf %{buildroot}
pushd mtce-control/cgts-mtce-control-1.0
make install buildroot=%{buildroot} _sysconfdir=/usr/local/etc _unitdir=/usr/lib/systemd/system _datarootdir=%{_datarootdir}
popd

%files
%defattr(-,root,root,-)
/usr/local/etc/init.d/goenabledControl

%files data
%defattr(-,root,root,-)
/usr/share/licenses/mtce-control-1.0/LICENSE