Summary:	Create a tree of hardlinks
Name:		hardlink
Version:	1.3
Release:	7%{?dist}
License:	GPLv2+
Vendor:         Microsoft Corporation
Distribution:   Mariner
URL:		https://pagure.io/hardlink
Source0:	https://pagure.io/hardlink/raw/master/f/hardlink.c
Source1:	https://pagure.io/hardlink/raw/master/f/hardlink.1
Source2:	https://www.gnu.org/licenses/old-licenses/gpl-2.0.txt
BuildRequires:  pcre2-devel, gcc

%description
hardlink is used to create a tree of hard links. It's used by kernel
installation to dramatically reduce the amount of disk space used by each
kernel package installed.

%prep
%setup -q -c -T
install -pm 644 %{SOURCE0} %{SOURCE2} .

%build
%{__cc} %{optflags} %{build_ldflags} hardlink.c -o hardlink -lpcre2-8

%install
install -D -m 644 %{SOURCE1} %{buildroot}%{_mandir}/man1/hardlink.1
install -D -m 755 hardlink %{buildroot}%{_sbindir}/hardlink

%files
%license gpl-2.0.txt
%{_sbindir}/hardlink
%{_mandir}/man1/hardlink.1*

%changelog
* Tue Sep 29 2020 Ruying Chen <v-ruyche@microsoft.com> - 1.3-7
- Initial import from CentOS8

* Mon Feb 19 2018 Francisco Javier Tsao Santín <tsao@gpul.org> - 1:1.3-6 
- Added gcc to build requirements

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Aug 19 2017 Tomasz Kłoczko <kloczek@fedoraproject.org> - 1:1.3-4
- remove manually added pcre2 requires (this is autogenerated)
- removed BuildRoot, %%defattr() and Group (new Fedora Packaging Guildline)
- do not use straight gcc and add use %%{__global_ldflags}
- use %%_licensedir is no longer needed
- minor cleanups:
-- reformat %%description to 80 col
-- added full URLs in Source fields
-- more macros
-- a bit simpler %%prep

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Apr 23 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 1:1.3-1
- Patch by Todd Lewis that adds option -x to exclude files with pcre lib 
- This patch solves RH Bugzilla ID's 955246 1322198 

* Thu Feb 16 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 1:1.2-1
- Fixed 32 bit build with gcc7 (RH Bugzilla ID 1422989)

* Sun Feb 12 2017 Francisco Javier Tsao Santín <tsao@gpul.org> - 1:1.1-4
- Fixed source url and description in spec file

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Sat Sep 03 2016 Kevin Fenzi <kevin@scrye.com> - 1.1-2
- Drop the kernel-utils obsolete that was added in 2005.

* Sun Jul 10 2016 Francisco Javier Tsao Santín <tsao@gpul.org> - 1:1.1-1
- Patch by Travers Carter for making hardlinking atomic

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:1.0-23
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-22
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-21
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jul 12 2014 Tom Callaway <spot@fedoraproject.org> - 1:1.0-20
- fix license handling

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-19
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-18
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Wed Apr 10 2013 Jan Zeleny <jzeleny@redhat.com> - 1:1.0-17
- Mention -f option in the man page

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sun Apr 15 2012 Jindrich Novy <jnovy@redhat.com> - 1:1.0-14
- do not allow to hardlink files across filesystems by default (#786719)
  (use -f option to override)

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Oct 21 2011 Jindrich Novy <jnovy@redhat.com> - 1:1.0-12
- fix possible buffer overflows, integer overflows (CVE-2011-3630 CVE-2011-3631 CVE-2011-3632)
- update man page

* Wed Mar  2 2011 Jindrich Novy <jnovy@redhat.com> - 1:1.0-11
- don't use mmap(2) to avoid failures on i386 with 1GB files and larger (#672917)
- fix package URL (#676962)

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:1.0-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Feb 25 2008 Jindrich Novy <jnovy@redhat.com> 1:1.0-7
- manual rebuild because of gcc-4.3 (#434188)

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1:1.0-6
- Autorebuild for GCC 4.3

* Thu Aug 23 2007 Jindrich Novy <jnovy@redhat.com> - 1:1.0-5
- update License
- rebuild for BuildID

* Mon Apr 23 2007 Jindrich Novy <jnovy@redhat.com> - 1:1.0-4
- include sources in debuginfo package (#230833)

* Mon Feb  5 2007 Jindrich Novy <jnovy@redhat.com> - 1:1.0-3
- merge review related spec fixes (#225881)

* Sun Oct 29 2006 Jindrich Novy <jnovy@redhat.com> - 1:1.0-2
- update docs to describe highest verbosity -vv option (#210816)
- use dist

* Wed Jul 12 2006 Jindrich Novy <jnovy@redhat.com> - 1:1.0-1.23
- remove ugly suffixes added by rebuild script

* Wed Jul 12 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0-1.21.2.1
- rebuild

* Fri Feb 10 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0-1.20.2
- bump again for double-long bug on ppc(64)

* Tue Feb 07 2006 Jesse Keating <jkeating@redhat.com> - 1:1.0-1.19.1
- rebuilt for new gcc4.1 snapshot and glibc changes

* Fri Dec 09 2005 Jesse Keating <jkeating@redhat.com>
- rebuilt

* Mon Nov 14 2005 Jindrich Novy <jnovy@redhat.com>
- more spec cleanup - thanks to Matthias Saou (#172968)
- use UTF-8 encoding in the source

* Mon Nov  7 2005 Jindrich Novy <jnovy@redhat.com>
- add hardlink man page
- add -h option
- use _sbindir instead of /usr/sbin directly
- don't warn because of uninitialized variable
- spec cleanup

* Fri Aug 26 2005 Dave Jones <davej@redhat.com>
- Document hardlink command line options. (Ville Skytta) (#161738)

* Wed Apr 27 2005 Jeremy Katz <katzj@redhat.com>
- don't try to hardlink 0 byte files (#154404)

* Fri Apr 15 2005 Florian La Roche <laroche@redhat.com>
- remove empty scripts

* Tue Mar  1 2005 Dave Jones <davej@redhat.com>
- rebuild for gcc4

* Tue Feb  8 2005 Dave Jones <davej@redhat.com>
- rebuild with -D_FORTIFY_SOURCE=2

* Tue Jan 11 2005 Dave Jones <davej@redhat.com>
- Add missing Obsoletes: kernel-utils

* Sat Dec 18 2004 Dave Jones <davej@redhat.com>
- Initial packaging, based upon kernel-utils.
