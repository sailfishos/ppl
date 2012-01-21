# 
# Do not Edit! Generated by:
# spectacle version 0.13~pre
# On 2010-02-24
# 
# >> macros
# << macros
%define keepstatic 1

Name:       ppl
Summary:    The Parma Polyhedra Library: a library of numerical abstractions
Version:    0.10.2
Release:    10
Group:      Development/Libraries
License:    GPLv3+
URL:        http://www.cs.unipr.it/ppl/
Source0:    ftp://ftp.cs.unipr.it/pub/ppl/releases/%{version}/%{name}-%{version}.tar.bz2
Source1:    ppl.hh
Source2:    ppl_c.h
Source3:    pwl.hh
Source100:  ppl.yaml
Patch0:     ppl-0.10.2-Makefile.patch
Patch1:     ppl-missing-macro.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  gmp-devel >= 4.1.3, m4 >= 1.4.8

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
The Parma Polyhedra Library (PPL) is a library for the manipulation of
(not necessarily closed) convex polyhedra and other numerical
abstractions.  The applications of convex polyhedra include program
analysis, optimized compilation, integer and combinatorial
optimization and statistical data-editing.  The Parma Polyhedra
Library comes with several user friendly interfaces, is fully dynamic
(available virtual memory is the only limitation to the dimension of
anything), written in accordance to all the applicable standards,
exception-safe, rather efficient, thoroughly documented, and free
software.  This package provides all what is necessary to run
applications using the PPL through its C and C++ interfaces.



%package pwl-devel
Summary:    Development tools for the Parma Watchdog Library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-pwl = %{version}-%{release}
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description pwl-devel
-devel
The header files, documentation and static libraries for developing
applications using the Parma Watchdog Library.


%package docs
Summary:    Documentation for the Parma Polyhedra Library
Group:      Documentation
Requires:   %{name} = %{version}-%{release}

%description docs
This package contains all the documentations required by programmers
using the Parma Polyhedra Library (PPL).
Install this package if you want to program with the PPL.


%package pwl-static
Summary:    Static archive for the Parma Watchdog Library
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-pwl-devel = %{version}-%{release}

%description pwl-static
-static
This package contains the static archive for the Parma Watchdog Library.


%package devel
Summary:    Development tools for the Parma Polyhedra Library C and C++ interfaces
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name} = %{version}-%{release}, gmp-devel >= 4.1.3

%description devel
The header files, Autoconf macro and minimal documentation for
developing applications using the Parma Polyhedra Library through
its C and C++ interfaces.


%package static
Summary:    Static archives for the Parma Polyhedra Library C and C++ interfaces
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-devel = %{version}-%{release}

%description static
The static archives for the Parma Polyhedra Library C and C++ interfaces.

%package pwl-docs
Summary:    Documentation for the Parma Watchdog Library
Group:      Documentation
Requires:   %{name} = %{version}-%{release}
Requires:   %{name}-pwl = %{version}-%{release}

%description pwl-docs
-docs
This package contains all the documentations required by programmers
using the Parma Watchdog Library (PWL).
Install this package if you want to program with the PWL.


%package pwl
Summary:    The Parma Watchdog Library: a C++ library for watchdog timers
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig

%description pwl
The Parma Watchdog Library (PWL) provides support for multiple,
concurrent watchdog timers on systems providing setitimer(2).  This
package provides all what is necessary to run applications using the
PWL.  The PWL is currently distributed with the Parma Polyhedra
Library, but is totally independent from it.



%prep
%setup -q -n %{name}-%{version}//
%patch0 -p1
%patch1 -p1
# >> setup
# << setup

%build
# >> build pre
# << build pre



# >> build post
CPPFLAGS="-I%{_includedir}/glpk"
CPPFLAGS="$CPPFLAGS -I%{_libdir}/gprolog-`gprolog --version 2>&1 | head -1 | sed -e "s/.* \([^ ]*\)$/\1/g"`/include"
CPPFLAGS="$CPPFLAGS -I`pl -dump-runtime-variables | grep PLBASE= | sed 's/PLBASE="\(.*\)";/\1/'`/include"
CPPFLAGS="$CPPFLAGS -I%{_includedir}/Yap"

CXXFLAGS=`echo $RPM_OPT_FLAGS|sed -e 's/-floop-interchange//g' -e 's/-floop-strip-mine//g' -e 's/-floop-block//g' -e 's/-ftree-loop-distribution//g'`
export CXXFLAGS
%configure --docdir=%{_datadir}/doc/%{name}-%{version} --enable-shared --disable-rpath --enable-interfaces="c++ c" CPPFLAGS="$CPPFLAGS"
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' Watchdog/libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' Watchdog/libtool
make %{?_smp_mflags}


# << build post
%install
rm -rf %{buildroot}
# >> install pre
# << install pre
# Please write install script under ">> install post"

# >> install post
rm -rf %{buildroot}
make DESTDIR=%{buildroot} INSTALL="%{__install} -p" install
rm -f %{buildroot}%{_libdir}/*.la %{buildroot}%{_libdir}/%{name}/*.la

# In order to avoid multiarch conflicts when installed for multiple
# architectures (e.g., i386 and x86_64), we rename the header files
# of the ppl-devel and ppl-pwl-devel packages.  They are substituted with
# ad-hoc switchers that select the appropriate header file depending on
# the architecture for which the compiler is compiling.

%ifarch %{arm}
normalized_arch=arm
%endif
%ifarch %{ix86}
normalized_arch=i386
%endif
%ifarch mipsel
normalized_arch=mipsel
%endif

mv %{buildroot}/%{_includedir}/ppl.hh %{buildroot}/%{_includedir}/ppl-${normalized_arch}.hh
install -m644 %{SOURCE1} %{buildroot}/%{_includedir}/ppl.hh
mv %{buildroot}/%{_includedir}/ppl_c.h %{buildroot}/%{_includedir}/ppl_c-${normalized_arch}.h
install -m644 %{SOURCE2} %{buildroot}/%{_includedir}/ppl_c.h
mv %{buildroot}/%{_includedir}/pwl.hh %{buildroot}/%{_includedir}/pwl-${normalized_arch}.hh
install -m644 %{SOURCE3} %{buildroot}/%{_includedir}/pwl.hh


# << install post

%clean
rm -rf %{buildroot}



%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%post pwl-devel -p /sbin/ldconfig

%postun pwl-devel -p /sbin/ldconfig





%post pwl -p /sbin/ldconfig

%postun pwl -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc %{_datadir}/doc/%{name}-%{version}/BUGS
%doc %{_datadir}/doc/%{name}-%{version}/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/CREDITS
%doc %{_datadir}/doc/%{name}-%{version}/NEWS
%doc %{_datadir}/doc/%{name}-%{version}/README
%doc %{_datadir}/doc/%{name}-%{version}/README.configure
%doc %{_datadir}/doc/%{name}-%{version}/TODO
%doc %{_datadir}/doc/%{name}-%{version}/gpl.txt
%{_libdir}/libppl.so.*
%{_libdir}/libppl_c.so.*
%{_bindir}/ppl-config
%{_mandir}/man1/ppl-config.1.gz
/usr/share/man/man1/ppl_lcdd.1.gz
/usr/bin/ppl_lcdd
#%dir %{_libdir}/%{name}
%dir %{_datadir}/doc/%{name}-%{version}
# << files


%files pwl-devel
%defattr(-,root,root,-)
# >> files pwl-devel
%doc Watchdog/doc/README.doc
%{_includedir}/pwl*.hh
%{_libdir}/libpwl.so
# << files pwl-devel

%files docs
%defattr(-,root,root,-)
# >> files docs
#%dir %{_datadir}/doc/%{name}-%{version}/
%doc %{_datadir}/doc/%{name}-%{version}/ChangeLog*
%doc %{_datadir}/doc/%{name}-%{version}/README.doc
%doc %{_datadir}/doc/%{name}-%{version}/fdl.*
%doc %{_datadir}/doc/%{name}-%{version}/gpl.pdf
%doc %{_datadir}/doc/%{name}-%{version}/gpl.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-c-interface-%{version}-html/
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-ocaml-interface-%{version}-html/
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-prolog-interface-%{version}-html/
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-c-interface-%{version}.pdf
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}.pdf
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-ocaml-interface-%{version}.pdf
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-prolog-interface-%{version}.pdf
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-%{version}.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-c-interface-%{version}.ps.gz
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-java-interface-%{version}.ps.gz
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-ocaml-interface-%{version}.ps.gz
#%doc %{_datadir}/doc/%{name}-%{version}/ppl-user-prolog-interface-%{version}.ps.gz
# << files docs

%files pwl-static
%defattr(-,root,root,-)
# >> files pwl-static
%{_libdir}/libpwl.a
# << files pwl-static

%files devel
%defattr(-,root,root,-)
# >> files devel
%{_includedir}/ppl*.hh
%{_includedir}/ppl_c*.h
%{_libdir}/libppl.so
%{_libdir}/libppl_c.so
%{_mandir}/man3/libppl.3.gz
%{_mandir}/man3/libppl_c.3.gz
%{_datadir}/aclocal/ppl.m4
%{_datadir}/aclocal/ppl_c.m4
# << files devel

%files static
%defattr(-,root,root,-)
# >> files static
%{_libdir}/libppl.a
%{_libdir}/libppl_c.a
# << files static

%files pwl-docs
%defattr(-,root,root,-)
# >> files pwl-docs
%doc %{_datadir}/doc/%{name}-%{version}/pwl/ChangeLog*
%doc %{_datadir}/doc/%{name}-%{version}/pwl/README.doc
%doc %{_datadir}/doc/%{name}-%{version}/pwl/fdl.*
%doc %{_datadir}/doc/%{name}-%{version}/pwl/gpl.ps.gz
%doc %{_datadir}/doc/%{name}-%{version}/pwl/gpl.pdf
%doc %{_datadir}/doc/%{name}-%{version}/pwl/pwl-user-0.7-html/
%doc %{_datadir}/doc/%{name}-%{version}/pwl/pwl-user-0.7.pdf
%doc %{_datadir}/doc/%{name}-%{version}/pwl/pwl-user-0.7.ps.gz
# << files pwl-docs

%files pwl
%defattr(-,root,root,-)
# >> files pwl
%doc %{_datadir}/doc/%{name}-%{version}/pwl/BUGS
%doc %{_datadir}/doc/%{name}-%{version}/pwl/COPYING
%doc %{_datadir}/doc/%{name}-%{version}/pwl/CREDITS
%doc %{_datadir}/doc/%{name}-%{version}/pwl/NEWS
%doc %{_datadir}/doc/%{name}-%{version}/pwl/README
%doc %{_datadir}/doc/%{name}-%{version}/pwl/gpl.txt
%{_libdir}/libpwl.so.*
%dir %{_datadir}/doc/%{name}-%{version}/pwl
# << files pwl

