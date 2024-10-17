%define module testoob
%define name python-%{module}
%define version 1.15
%define release 2

Summary: Advanced Python unit testing framework
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{module}-%{version}.tar.bz2
License: Apache License
Group: Development/Python
Url: https://testoob.sourceforge.net
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

%files
%defattr(-,root,root)
%doc README docs/*
%_bindir/*
%py_puresitedir/*


%changelog
* Wed Nov 17 2010 Funda Wang <fwang@mandriva.org> 1.15-1mdv2011.0
+ Revision: 598149
- rebuild for py 2.7

* Sun Jan 10 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.15-1mdv2010.1
+ Revision: 489194
- update to new version 1.15

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.13-6mdv2010.0
+ Revision: 442511
- rebuild

* Fri Jan 02 2009 Funda Wang <fwang@mandriva.org> 1.13-5mdv2009.1
+ Revision: 323414
- rebuild

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 1.13-4mdv2009.0
+ Revision: 259832
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 1.13-3mdv2009.0
+ Revision: 247697
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Nov 07 2007 Lev Givon <lev@mandriva.org> 1.13-1mdv2008.1
+ Revision: 106752
- import python-testoob


* Sun Nov 4 2007 Lev Givon <lev@mandriva.org> 1.13-1mdv2008.0
- Initial Mandriva package.
