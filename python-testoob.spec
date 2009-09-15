%define module testoob
%define name python-%{module}
%define version 1.13
%define release %mkrel 6

Summary: Advanced Python unit testing framework
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.tar.bz2
License: Apache License
Group: Development/Python
Url: http://testoob.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: noarch
BuildRequires: python-devel

%description
Testoob is an advanced Python unit testing framework that integrates
effortlessly with Python's standard 'unittest' module. It is designed
and built to be easy to use and extend.

%prep
%setup -q -n %{module}-%{version}

%build
%__python setup.py build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot} --record=INSTALLED_FILES

%clean
%__rm -rf %{buildroot}

%files -f INSTALLED_FILES
%defattr(-,root,root)
%doc README docs/*

