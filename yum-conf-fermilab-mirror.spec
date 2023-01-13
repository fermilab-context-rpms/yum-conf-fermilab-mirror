Name:		yum-conf-fermilab-mirror
Version:	1.2
Release:	2%{?dist}
Summary:	yum/dnf repo files that use the Fermilab mirrors

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/yum-conf-fermilab-mirror

BuildArch:	noarch
Source0:	yum-conf-fermilab-mirror-sources.tar.gz

# Top level package should require software specific packages
Requires:	(%{name}-almalinux == %{version}-%{release} if almalinux-repos)
Requires:	(%{name}-centos-stream == %{version}-%{release} if centos-stream-repos)
Requires:	(%{name}-epel == %{version}-%{release} if epel-release)
Requires:	(%{name}-epel-next == %{version}-%{release} if epel-next-release)

%description
This package deploys yum/dnf repo files that use the Fermilab mirrors.

%package almalinux
Summary:        yum/dnf repo files for AlmaLinux
Requires:       dnf dnf-utils
Requires:       almalinux-repos

%description almalinux
This package deploys yum/dnf repo files for AlmaLinux that use the Fermilab mirrors.

%package centos-stream
Summary:	yum/dnf repo files for CentOS Stream
Requires:	dnf dnf-utils
Requires:	centos-stream-repos

%description centos-stream
This package deploys yum/dnf repo files for CentOS Stream that use the Fermilab mirrors.

%package epel
Summary:	yum/dnf repo files for EPEL
Requires:	dnf dnf-utils
Requires:	system-release(releasever) redhat-release epel-release

%description epel
This package deploys yum/dnf repo files for EPEL that use the Fermilab mirrors.

%package epel-next
Summary:        yum/dnf repo files for EPEL-Next
Requires:       dnf dnf-utils
Requires:       system-release(releasever) redhat-release epel-next-release

%description epel-next
This package deploys yum/dnf repo files for EPEL-Next that use the Fermilab mirrors.


%prep
%setup -n repos


%build


%install
# for almalinux
%{__install} -D fnal-almalinux.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fnal-almalinux.repo

# for centos-stream
%{__install} -D fnal-centos-stream.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fnal-centos-stream.repo

# for epel
%{__install} -D fnal-epel.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fnal-epel.repo

# for epel-next
%{__install} -D fnal-epel-next.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fnal-epel-next.repo


#####################################################################
#####################################################################
%files
%defattr(0644,root,root,0755)

%files almalinux
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/yum.repos.d/fnal-almalinux.repo

%files centos-stream
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/yum.repos.d/fnal-centos-stream.repo

%files epel
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/yum.repos.d/fnal-epel.repo

%files epel-next
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/yum.repos.d/fnal-epel-next.repo


#####################################################################
%changelog
* Thu Jan 13 2022 Pat Riehecky <riehecky@fnal.gov> 1.2-2
- Fix dupe name for epel-next-testing

* Thu Jan 12 2022 Pat Riehecky <riehecky@fnal.gov> 1.2-1
- Fix logic swap for epel/epel-next

* Mon Jan 9 2022 Pat Riehecky <riehecky@fnal.gov> 1.1-2
- Fix typo in alma linux extras repo

* Tue Nov 29 2022 Pat Riehecky <riehecky@fnal.gov> 1.1-1
- More consistent names for repos and repo files
- Add almalinux package
- split out epel-next repo
- fix deps for epel so we get the gpg key

* Sat Apr 30 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2.1
- Fix install typo

* Fri Apr 29 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2
- Add addon product repos

* Fri Apr 29 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build
