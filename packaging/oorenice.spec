Name:           oorenice
Version:        0.1.0
Release:        1%{?dist}
Summary:        Alters priority of existing running process groups and user sessions.
License:        ASL 2.0
URL:            https://github.com/openOODA-tools/oorenice
Source0:        oorenice-linux-x86_64
Source1:        uninstall.sh
BuildArch:      x86_64
Requires:       glibc

%description
oorenice is a sovereign, capability-bounded ACTIVE RENICER written
in pure openOODA, featuring zero ambient authority, oote color themes,
and an MCP stdio server.

%install
mkdir -p %{buildroot}/usr/bin
install -m 0755 %{SOURCE0} %{buildroot}/usr/bin/oorenice
install -m 0755 %{SOURCE1} %{buildroot}/usr/bin/oorenice-uninstall

%files
/usr/bin/oorenice
/usr/bin/oorenice-uninstall

%changelog
* Wed Oct 07 2026 openOODA-tools <ops@openooda.org> - 0.1.0-1
- Initial sovereign blueprint scaffolding
