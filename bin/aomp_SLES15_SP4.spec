Summary: AMD OpenMP Compiler Suite
Name: aomp_SLES15_SP4
Version: __VERSION1
Release: __VERSION3_MOD
Source: ~/rpm/SOURCES/aomp_SLES15_SP4.tar.gz
URL: https://github.com/ROCm-Developer-Tools/aomp
License: MIT and ASL 2.0
Group: System/Base
Vendor: AMD

%define __os_install_post %{nil}
%define __requires_exclude ^libcuda\\.so\\..*

%description
 The AMD OpenMP Compiler (AOMP) is an experimental LLVM compiler
 suite for offloading to either Radeon GPUs or Nvidia GPUs.
 AOMP requires either rocm, cuda, or both.

%prep
%setup -n %{name}

%build

%install
echo "INSTALL RUNNING IN $PWD"
mkdir -p $RPM_BUILD_ROOT/usr/lib
rsync -a usr/lib $RPM_BUILD_ROOT/usr

%clean
echo "CLEAN RUNNING IN $PWD"
rm -rf $RPM_BUILD_ROOT
echo rm -rf %{_tmppath}/%{name}
rm -rf %{_tmppath}/%{name}
echo rm -rf %{_topdir}/BUILD/%{name}
rm -rf %{_topdir}/BUILD/%{name}

%post
echo "POST INSTALL SCRIPT FROM spec file RUNNING IN $PWD"
if [ -L /usr/lib/aomp ] ; then rm /usr/lib/aomp ; fi
ln -sf /usr/lib/aomp___VERSION2_STRING /usr/lib/aomp
if [ -L /usr/bin/aompcc ] ; then rm /usr/bin/aompcc ; fi
ln -sf /usr/lib/aomp/bin/aompcc /usr/bin/aompcc
if [ -L /usr/bin/aompversion ] ; then rm /usr/bin/aompversion ; fi
ln -sf /usr/lib/aomp/bin/aompversion /usr/bin/aompversion
if [ -L /usr/bin/mymcpu ] ; then rm /usr/bin/mymcpu ; fi
ln -sf /usr/lib/aomp/bin/mymcpu /usr/bin/mymcpu
if [ -L /usr/bin/mygpu ] ; then rm /usr/bin/mygpu ; fi
ln -sf /usr/lib/aomp/bin/mygpu /usr/bin/mygpu
if [ -L /usr/bin/cloc.sh ] ; then rm /usr/bin/cloc.sh ; fi
ln -sf /usr/lib/aomp/bin/cloc.sh /usr/bin/cloc.sh
if [ -L /usr/bin/gpurun ] ; then rm /usr/bin/gpurun ; fi
ln -sf /usr/lib/aomp/bin/gpurun /usr/bin/gpurun
if [ -f /etc/profile.d/aomp.sh ] ; then rm /etc/profile.d/aomp.sh ; fi
echo "export AOMP=/usr/lib/aomp" >/etc/profile.d/aomp.sh
if [ -f /etc/profile.d/aomp.csh ] ; then rm /etc/profile.d/aomp.csh ; fi
echo "setenv AOMP /usr/lib/aomp" >/etc/profile.d/aomp.csh
echo "DONE POST INSTALL SCRIPT FROM spec file RUNNING IN $PWD"

%files
%defattr(-,root,root)
%{_prefix}/lib/aomp___VERSION2_STRING

%postun
rm /usr/lib/aomp
rm /usr/bin/aompcc
rm /usr/bin/aompversion
rm /usr/bin/gpurun
rm /usr/bin/mymcpu
rm /usr/bin/mygpu
rm /usr/bin/cloc.sh
rm /etc/profile.d/aomp.sh
rm /etc/profile.d/aomp.csh

%changelog
* Thu Jun 13 2019 Greg Rodgers <gregory.rodgers@amd.com>
