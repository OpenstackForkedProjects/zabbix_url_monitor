%{!?python_sitelib: %define python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print get_python_lib()")}

Name:           url_monitor
Version:        %(%{__python} -c "import url_monitor.packaging as namespace; print(namespace.version)")
Release:        1%{?dist}
Group:          Applications/Systems
Summary:        This is an external script for zabbix for monitoring restful endpoints for data.

License:        ASLv2
URL:            %(%{__python} -c "import url_monitor.packaging as namespace; print(namespace.url)")
Source0:        %{name}-%{version}.tar.gz

BuildArch:      noarch
BuildRoot:      %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)
BuildRequires:  python-setuptools
Requires(pre):  shadow-utils
%(%{__python} -c "import sys; import url_monitor.packaging as namespace; x = lambda x: sys.stdout.write(\" \".join(x) + \"\"); sys.stdout.write(\"Requires: \"); str(x(namespace.rpm_requires))")

%define service_name %{name}d

%description
%(%{__python} -c "import url_monitor.packaging as namespace; print(namespace.long_description)")

%prep
%setup -q -n %{name}-%{version}

%build

%pre

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_localstatedir}/log/%{name}
mkdir -p %{buildroot}%{_localstatedir}/lib/%{name}
%post

%preun

%postun

%files
%doc README.md
%config(noreplace) %attr(0644,root,root) %{_sysconfdir}/url_monitor.yaml
%{python_sitelib}/%{name}
%{python_sitelib}/%{name}*.egg-info
%attr(0755,-,-) %{_bindir}/%{name}

%changelog
* Fri Apr 29 2016 Jonathan Kelley <jon.kelley@rackspace.com> - 0.8.5-1
- Fixes to work better when singleton doesnt take, like on py2.6

