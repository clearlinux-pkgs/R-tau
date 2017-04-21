#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-tau
Version  : 0.0.19
Release  : 30
URL      : http://cran.r-project.org/src/contrib/tau_0.0-19.tar.gz
Source0  : http://cran.r-project.org/src/contrib/tau_0.0-19.tar.gz
Summary  : Text Analysis Utilities
Group    : Development/Tools
License  : GPL-2.0
Requires: R-tau-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-tau package.
Group: Libraries

%description lib
lib components for the R-tau package.


%prep
%setup -q -c -n tau

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1492799667

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1492799667
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library tau
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library tau


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/tau/DESCRIPTION
/usr/lib64/R/library/tau/INDEX
/usr/lib64/R/library/tau/Meta/Rd.rds
/usr/lib64/R/library/tau/Meta/features.rds
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

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/tau/libs/tau.so
