#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-jgit
Version  : 2.0.0.201206130900.r
Release  : 5
URL      : https://github.com/eclipse/jgit/archive/v2.0.0.201206130900-r.tar.gz
Source0  : https://github.com/eclipse/jgit/archive/v2.0.0.201206130900-r.tar.gz
Source1  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit-parent/2.0.0.201206130900-r/org.eclipse.jgit-parent-2.0.0.201206130900-r.pom
Source2  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit-parent/3.2.0.201312181205-r/org.eclipse.jgit-parent-3.2.0.201312181205-r.pom
Source3  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r/org.eclipse.jgit-2.0.0.201206130900-r.jar
Source4  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r/org.eclipse.jgit-2.0.0.201206130900-r.pom
Source5  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r/org.eclipse.jgit-3.2.0.201312181205-r.jar
Source6  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r/org.eclipse.jgit-3.2.0.201312181205-r.pom
Source7  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r/org.eclipse.jgit-5.3.0.201903130848-r.jar
Source8  : https://repo.maven.apache.org/maven2/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r/org.eclipse.jgit-5.3.0.201903130848-r.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause EPL-1.0
Requires: mvn-jgit-data = %{version}-%{release}
Requires: mvn-jgit-license = %{version}-%{release}
BuildRequires : apache-maven
BuildRequires : buildreq-mvn

%description
== Java GIT ==
This package is licensed under the BSD.
org.eclipse.jgit/
A pure Java library capable of being run standalone, with no
additional support libraries.  Some JUnit tests are provided
to exercise the library.  The library provides functions to
read and write a GIT formatted repository.

%package data
Summary: data components for the mvn-jgit package.
Group: Data

%description data
data components for the mvn-jgit package.


%package license
Summary: license components for the mvn-jgit package.
Group: Default

%description license
license components for the mvn-jgit package.


%prep
%setup -q -n jgit-2.0.0.201206130900-r

%build

%install
mkdir -p %{buildroot}/usr/share/package-licenses/mvn-jgit
cp LICENSE %{buildroot}/usr/share/package-licenses/mvn-jgit/LICENSE
cp org.eclipse.jgit.packaging/org.eclipse.jgit.feature/license.html %{buildroot}/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.feature_license.html
cp org.eclipse.jgit.packaging/org.eclipse.jgit.pgm.feature/license.html %{buildroot}/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.pgm.feature_license.html
cp org.eclipse.jgit.packaging/org.eclipse.jgit.pgm.source.feature/license.html %{buildroot}/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.pgm.source.feature_license.html
cp org.eclipse.jgit.packaging/org.eclipse.jgit.source.feature/license.html %{buildroot}/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.source.feature_license.html
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit-parent/2.0.0.201206130900-r
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit-parent/2.0.0.201206130900-r/org.eclipse.jgit-parent-2.0.0.201206130900-r.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit-parent/3.2.0.201312181205-r
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit-parent/3.2.0.201312181205-r/org.eclipse.jgit-parent-3.2.0.201312181205-r.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r/org.eclipse.jgit-2.0.0.201206130900-r.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r/org.eclipse.jgit-2.0.0.201206130900-r.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r/org.eclipse.jgit-3.2.0.201312181205-r.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r/org.eclipse.jgit-3.2.0.201312181205-r.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r/org.eclipse.jgit-5.3.0.201903130848-r.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r
cp %{SOURCE8} %{buildroot}/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r/org.eclipse.jgit-5.3.0.201903130848-r.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit-parent/2.0.0.201206130900-r/org.eclipse.jgit-parent-2.0.0.201206130900-r.pom
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit-parent/3.2.0.201312181205-r/org.eclipse.jgit-parent-3.2.0.201312181205-r.pom
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r/org.eclipse.jgit-2.0.0.201206130900-r.jar
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/2.0.0.201206130900-r/org.eclipse.jgit-2.0.0.201206130900-r.pom
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r/org.eclipse.jgit-3.2.0.201312181205-r.jar
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/3.2.0.201312181205-r/org.eclipse.jgit-3.2.0.201312181205-r.pom
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r/org.eclipse.jgit-5.3.0.201903130848-r.jar
/usr/share/java/.m2/repository/org/eclipse/jgit/org.eclipse.jgit/5.3.0.201903130848-r/org.eclipse.jgit-5.3.0.201903130848-r.pom

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mvn-jgit/LICENSE
/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.feature_license.html
/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.pgm.feature_license.html
/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.pgm.source.feature_license.html
/usr/share/package-licenses/mvn-jgit/org.eclipse.jgit.packaging_org.eclipse.jgit.source.feature_license.html
