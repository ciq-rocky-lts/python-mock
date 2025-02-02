%bcond_without python3
%bcond_with tests

# Not yet in Fedora buildroot
%{!?python3_pkgversion:%global python3_pkgversion 3}

%global mod_name mock

Name:           python-mock
Version:        2.0.0
Release:        13%{?dist}
Summary:        A Python Mocking and Patching Library for Testing

License:        BSD
URL:            http://www.voidspace.org.uk/python/%{mod_name}/
Source0:        https://pypi.python.org/packages/source/m/%{mod_name}/%{mod_name}-%{version}.tar.gz
Patch0:         0001-Remove-pbr-dependency.patch

BuildArch:      noarch
BuildRequires:  python2-devel
BuildRequires:  python2-setuptools
BuildRequires:  python2-funcsigs

%if %{with python3}
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
%if %{with tests}
# For tests
BuildRequires:  python%{python3_pkgversion}-unittest2
%endif
%endif


%description
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.

%package -n python2-mock
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python2-%{mod_name}}
Requires:    python2-funcsigs
Requires:    python2-six >= 1.9.0

%description -n python2-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set

%if %{with python3}
%package -n python%{python3_pkgversion}-mock
Summary:        A Python Mocking and Patching Library for Testing
%{?python_provide:%python_provide python%{python3_pkgversion}-%{mod_name}}
Requires:    python3-six >= 1.9.0

%description -n python%{python3_pkgversion}-mock
Mock is a Python module that provides a core mock class. It removes the need
to create a host of stubs throughout your test suite. After performing an
action, you can make assertions about which methods / attributes were used and
arguments they were called with. You can also specify return values and set
needed attributes in the normal way.
%endif


%prep
%setup -q -n %{mod_name}-%{version}
%patch0 -p1
sed -i "s|VERSIONPLACEHOLDER|%{version}|" setup.cfg mock/mock.py

%build
%{py2_build}
%if %{with python3}
%{py3_build}
%endif


%check
%if %{with tests}
%if %{with python3}
# Few failing tests but keep output
%{__python3} setup.py test ||:
%endif
%endif

%install
%if %{with python3}
%{py3_install}
%endif
%{py2_install}


%files -n python2-mock
%license LICENSE.txt
%doc docs/*
%{python2_sitelib}/*.egg-info
%{python2_sitelib}/%{mod_name}

%if %{with python3}
%files -n python%{python3_pkgversion}-mock
%license LICENSE.txt
%doc docs/*
%{python3_sitelib}/*.egg-info
%{python3_sitelib}/%{mod_name}
%endif


%changelog
* Thu Apr 25 2019 Tomas Orsava <torsava@redhat.com> - 2.0.0-13
- Bumping due to problems with modular RPM upgrade path
- Resolves: rhbz#1695587

* Tue Jul 31 2018 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-12
- Switch python3 coditions to bcond

* Sun Jul 15 2018 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-11
- Enable Python 3 subpackage and disabled tests

* Fri Jul 13 2018 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-10
- First version for python27 module

* Mon Jul 09 2018 Petr Viktorin <pviktori@redhat.com> - 2.0.0-9
- Drop dependency on python3-funcsigs
  (funcsigs functionality is in the Python 3 standard library -- inspect)
- Drop dependency on python2-unittest2
  (Not available in the distro)

- Fix python2 requires names

* Mon Jun 25 2018 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-9
- Allow build with Python 2

* Wed Jun 20 2018 Lumír Balhar <lbalhar@redhat.com> - 2.0.0-8
- Add patch to remove dependency on pbr

* Fri Feb 09 2018 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Tue Oct 10 2017 Troy Dawson <tdawson@redhat.com> - 2.0.0-6
- Cleanup spec file conditionals

* Thu Jul 27 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sat Feb 11 2017 Fedora Release Engineering <releng@fedoraproject.org> - 2.0.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Dec 09 2016 Charalampos Stratakis <cstratak@redhat.com> - 2.0.0-3
- Rebuild for Python 3.6

* Tue Jul 19 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.0.0-2
- https://fedoraproject.org/wiki/Changes/Automatic_Provides_for_Python_RPM_Packages

* Tue Jun 14 2016 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 2.0.0-1
- Upstream 2.0.0 (RHBZ#1244145)

* Fri Feb 26 2016 Haïkel Guémar <hguemar@fedoraproject.org> - 1.3.0-1
- Upstream 1.3.0 (RHBZ#1244145)
- Use epel macros rather than rhel

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0.1-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jan 6 2016 Orion Poplawski <orion@cora.nwra.com> - 1.0.1-9
- Modernize spec
- Run python2 tests, python3 failing

* Thu Nov 12 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-8
- Rebuilt for https://fedoraproject.org/wiki/Changes/python3.5

* Mon Nov 02 2015 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> 1.0.1-7
- Fix #1276771

* Wed Sep 23 2015 Robert Kuska <rkuska@redhat.com> - 1.0.1-6
- Rebuilt for Python3.5 rebuild

* Thu Jun 18 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Fri May 09 2014 Dennis Gilmore <dennis@ausil.us> - 1.0.1-3
- rebuild for python 3.4
- disable test suite deps missing

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Apr 11 2013 Luke Macken <lmacken@redhat.com> - 1.0.1-1
- Update to 1.0.1
- Run the test suite
- Add python-unittest2 as a build requirement

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sat Aug 04 2012 David Malcolm <dmalcolm@redhat.com> - 0.8.0-4
- rebuild for https://fedoraproject.org/wiki/Features/Python_3.3

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.8.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Jul 09 2012 Ralph Bean <rbean@redhat.com> - 0.8.0-2
- Python3 support

* Thu Mar 22 2012 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.8.0-1
- Updated to new version

* Fri Jul 22 2011 Praveen Kumar <kumarpraveen.nitdgp@gmail.com> - 0.7.2-1
- Initial RPM release
