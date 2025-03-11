#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Fixture configuration utils for py.test
Summary(pl.UTF-8):	Narzędzia do konfiguracji osprzętu dla py.test
Name:		python-pytest-fixture-config
Version:	1.7.0
Release:	6
License:	MIT
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/pytest-fixture-config/
Source0:	https://files.pythonhosted.org/packages/source/p/pytest-fixture-config/pytest-fixture-config-%{version}.tar.gz
# Source0-md5:	ddfc66f7246535c2c238c72f3463b138
URL:		https://github.com/manahl/pytest-plugins
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
BuildRequires:	python-setuptools_git
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
BuildRequires:	python3-setuptools_git
%if %{with tests}
BuildRequires:	python-pytest
BuildRequires:	python-six
%endif
%endif
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Simple configuration objects for Py.test fixtures. Allows you to skip
tests when their required config variables aren't set.

%description -l pl.UTF-8
Proste obiekty konfiguracyjne do osprzętu (fixtures) Py.test.
Pozwalają pomijać testy, kiedy wymagane przez nie zmienne nie są
ustawione.

%package -n python3-pytest-fixture-config
Summary:	Fixture configuration utils for py.test
Summary(pl.UTF-8):	Narzędzia do konfiguracji osprzętu dla py.test
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-pytest-fixture-config
Simple configuration objects for Py.test fixtures. Allows you to skip
tests when their required config variables aren't set.

%description -n python3-pytest-fixture-config -l pl.UTF-8
Proste obiekty konfiguracyjne do osprzętu (fixtures) Py.test.
Pozwalają pomijać testy, kiedy wymagane przez nie zmienne nie są
ustawione.

%prep
%setup -q -n pytest-fixture-config-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%{py_sitescriptdir}/pytest_fixture_config.py[co]
%{py_sitescriptdir}/pytest_fixture_config-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-pytest-fixture-config
%defattr(644,root,root,755)
%doc CHANGES.md LICENSE README.md
%{py3_sitescriptdir}/pytest_fixture_config.py
%{py3_sitescriptdir}/__pycache__/pytest_fixture_config.cpython-*.py[co]
%{py3_sitescriptdir}/pytest_fixture_config-%{version}-py*.egg-info
%endif
