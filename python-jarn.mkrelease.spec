%define	oname	jarn.mkrelease

Summary:	Python egg releaser
Name:		python-%{oname}
Version:	3.0.1
Release:	%mkrel 2
License:	BSD
Group:		Development/Other
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Source0:	%{oname}-%{version}.tar.xz
Patch0:		jarn.mkrelease-3.0.1-drop-non-existent-dependencies.patch
URL:		http://pypi.python.org/pypi/jarn.mkrelease/
BuildArch:	noarch
Requires:	python-setuptools

%description
mkrelease is a no-frills Python egg releaser. It was created to take the cumber
out of building and distributing Python eggs.

%prep
%setup -q -n %{oname}-%{version}
%patch0 -p1 -b .bogusdeps~

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root, root)
%doc CHANGES.txt README.txt
%{_bindir}/mkrelease
%dir %{python_sitelib}/jarn
%dir %{python_sitelib}/jarn/mkrelease
%{python_sitelib}/jarn/mkrelease/*.py*
%dir %{python_sitelib}/jarn/mkrelease/tests
%{python_sitelib}/jarn/mkrelease/tests/*.txt
%{python_sitelib}/jarn/mkrelease/tests/*.py*
%{python_sitelib}/jarn/mkrelease/tests/*.zip
%{python_sitelib}/%{oname}-%{version}-py%{python_version}.egg-info
%{python_sitelib}/%{oname}-%{version}-py%{python_version}-nspkg.pth

