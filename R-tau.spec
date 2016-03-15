#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tau
Version  : 0.0
Release  : 16
URL      : http://cran.r-project.org/src/contrib/tau_0.0-18.tar.gz
Source0  : http://cran.r-project.org/src/contrib/tau_0.0-18.tar.gz
Summary  : Text Analysis Utilities
Group    : Development/Tools
License  : GPL-2.0
BuildRequires : clr-R-helpers

%description
No detailed description available

%prep
%setup -q -c -n tau

%build

%install
rm -rf %{buildroot}
export LANG=C
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --build  -l %{buildroot}/usr/lib64/R/library tau
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=intel.com,localhost
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tau


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tau/DESCRIPTION
/usr/lib64/R/library/tau/INDEX
/usr/lib64/R/library/tau/Meta/Rd.rds
/usr/lib64/R/library/tau/Meta/hsearch.rds
/usr/lib64/R/library/tau/Meta/links.rds
/usr/lib64/R/library/tau/Meta/nsInfo.rds
/usr/lib64/R/library/tau/Meta/package.rds
/usr/lib64/R/library/tau/NAMESPACE
/usr/lib64/R/library/tau/R/sysdata.rdb
/usr/lib64/R/library/tau/R/sysdata.rdx
/usr/lib64/R/library/tau/R/tau
/usr/lib64/R/library/tau/R/tau.rdb
/usr/lib64/R/library/tau/R/tau.rdx
/usr/lib64/R/library/tau/help/AnIndex
/usr/lib64/R/library/tau/help/aliases.rds
/usr/lib64/R/library/tau/help/paths.rds
/usr/lib64/R/library/tau/help/tau.rdb
/usr/lib64/R/library/tau/help/tau.rdx
/usr/lib64/R/library/tau/html/00Index.html
/usr/lib64/R/library/tau/html/R.css
/usr/lib64/R/library/tau/libs/symbols.rds
/usr/lib64/R/library/tau/libs/tau.so
