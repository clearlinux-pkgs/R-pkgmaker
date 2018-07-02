#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-pkgmaker
Version  : 0.27
Release  : 12
URL      : https://cran.r-project.org/src/contrib/pkgmaker_0.27.tar.gz
Source0  : https://cran.r-project.org/src/contrib/pkgmaker_0.27.tar.gz
Summary  : Development Utilities for R Packages
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-bibtex
Requires: R-devtools
Requires: R-registry
Requires: R-rmarkdown
Requires: R-xtable
BuildRequires : R-bibtex
BuildRequires : R-devtools
BuildRequires : R-registry
BuildRequires : R-rmarkdown
BuildRequires : R-xtable
BuildRequires : clr-R-helpers

%description
development. It currently provides managers for multiple package specific
    options and registries, vignette, unit test and bibtex related utilities.
    It serves as a base package for packages like NMF, RcppOctave, doRNG, and
    as an incubator package for other general purposes utilities, that will
    eventually be packaged separately.
    It is still under heavy development and changes in the interface(s) are
    more than likely to happen.

%prep
%setup -q -c -n pkgmaker

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1527428811

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1527428811
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgmaker
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512 " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize -mprefer-vector-width=512  " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgmaker
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library pkgmaker
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library pkgmaker|| : 
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/pkgmaker/DESCRIPTION
/usr/lib64/R/library/pkgmaker/INDEX
/usr/lib64/R/library/pkgmaker/Meta/Rd.rds
/usr/lib64/R/library/pkgmaker/Meta/features.rds
/usr/lib64/R/library/pkgmaker/Meta/hsearch.rds
/usr/lib64/R/library/pkgmaker/Meta/links.rds
/usr/lib64/R/library/pkgmaker/Meta/nsInfo.rds
/usr/lib64/R/library/pkgmaker/Meta/package.rds
/usr/lib64/R/library/pkgmaker/NAMESPACE
/usr/lib64/R/library/pkgmaker/R/pkgmaker
/usr/lib64/R/library/pkgmaker/R/pkgmaker.rdb
/usr/lib64/R/library/pkgmaker/R/pkgmaker.rdx
/usr/lib64/R/library/pkgmaker/cleveref.sty
/usr/lib64/R/library/pkgmaker/help/AnIndex
/usr/lib64/R/library/pkgmaker/help/aliases.rds
/usr/lib64/R/library/pkgmaker/help/paths.rds
/usr/lib64/R/library/pkgmaker/help/pkgmaker.rdb
/usr/lib64/R/library/pkgmaker/help/pkgmaker.rdx
/usr/lib64/R/library/pkgmaker/html/00Index.html
/usr/lib64/R/library/pkgmaker/html/R.css
/usr/lib64/R/library/pkgmaker/package.mk
/usr/lib64/R/library/pkgmaker/vignette.mk
