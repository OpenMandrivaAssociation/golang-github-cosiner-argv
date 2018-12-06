# https://github.com/cosiner/argv
%global goipath         github.com/cosiner/argv
%global commit          13bacc38a0a5e0eba18b6f03cbb15dc5d4243b04

%gometa

Name:           %{goname}
Version:        0
Release:        0.3%{?dist}
Summary:        Split command line string into arguments array
License:        MIT
URL:            %{gourl}
Source0:        %{gosource}

%description
%{summary}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{summary}

This package contains library source intended for building other packages which
use import path with %{goipath} prefix.


%prep
%forgesetup


%install
%goinstall


%check
%gochecks


%files devel -f devel.file-list
%license LICENSE
%doc README.md


%changelog
* Fri Nov 02 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0-0.3.20180815git13bacc3
- Cleanup SPEC

* Tue Oct 23 2018 Nicolas Mailhot <nim@fedoraproject.org> - 0-0.2.20180815git13bacc3
- redhat-rpm-config-123 triggers bugs in gosetup, remove it from Go spec files as it’s just an alias
- https://lists.fedoraproject.org/archives/list/devel@lists.fedoraproject.org/message/RWD5YATAYAFWKIDZBB7EB6N5DAO4ZKFM/

* Wed Aug 15 2018 Elliott Sales de Andrade <quantum.analyst@gmail.com> - 0-0.1.20180815git13bacc3
- First package for Fedora
