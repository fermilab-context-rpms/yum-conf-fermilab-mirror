Name:		yum-conf-fermilab-mirror
Version:	1.0
Release:	2.1%{?dist}
Summary:	yum/dnf repo files that use the Fermilab mirrors

Group:		Fermilab
License:	GPL
URL:		https://github.com/fermilab-context-rpms/yum-conf-fermilab-mirror

BuildArch:	noarch
Source0:	yum-conf-fermilab-mirror-sources.tar.gz

# Top level package should require software specific packages
Requires:	(%{name}-centos-stream == %{version}-%{release} if centos-stream-repos)
Requires:	(%{name}-epel == %{version}-%{release} if epel-release)

%description
This package deploys yum/dnf repo files that use the Fermilab mirrors.

%package centos-stream
Summary:	yum/dnf repo files for CentOS Stream
Requires:	dnf dnf-utils
Requires:	centos-stream-repos

%description centos-stream
This package deploys yum/dnf repo files for CentOS Stream that use the Fermilab mirrors.

%package epel
Summary:	yum/dnf repo files for EPEL
Requires:	dnf dnf-utils
Requires:	system-release(releasever) redhat-release

%description epel
This package deploys yum/dnf repo files for EPEL that use the Fermilab mirrors.


%prep
%setup -n repos


%build


%install
# for stream
%{__install} -D fnal-centos.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fnal-centos.repo

# for epel
%{__install} -D fnal-epel.repo %{buildroot}%{_sysconfdir}/yum.repos.d/fnal-epel.repo


#####################################################################
#####################################################################
%files
%defattr(0644,root,root,0755)

%files centos-stream
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/yum.repos.d/fnal-centos.repo

%files epel
%defattr(0644,root,root,0755)
%config %{_sysconfdir}/yum.repos.d/fnal-epel.repo

#####################################################################
%changelog
* Sat Apr 30 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2.1
- Fix install typo

* Fri Apr 29 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-2
- Add addon product repos

* Fri Apr 29 2022 Pat Riehecky <riehecky@fnal.gov> 1.0-1
- Initial build
