# TODO:
# - fix bash substitution
#
%bcond_with	java_sun
#
Summary:	OpenJDK and GNU Classpath code
SummarY(pl.UTF-8):	Kod OpenJDK i GNU Classpath
Name:		icedtea
Version:	1.6
Release:	0.1
License:	GPL
Group:		Development/Languages/Java
Source0:	http://icedtea.classpath.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	99343f82b3a642a3be3e96816608ae23
# Create this one by running make openjdk-dist (needs mercurial + mercurial forest extension)
Source1:	openjdk-b24.zip
# Source1-md5:	339618d385930f6dc07a7524541cae54
URL:		http://icedtea.classpath.org/wiki/Main_Page
BuildRequires:	alsa-lib-devel
BuildRequires:	bash
BuildRequires:	cups-devel
BuildRequires:	eclipse-ecj
BuildRequires:	freetype-devel
BuildRequires:	gcc-java
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	jdk
BuildRequires:	libgcj
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	motif-devel
BuildRequires:	unzip
BuildRequires:	xalan-j
BuildRequires:	xerces-j
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xulrunner-devel
BuildRequires:	zlib-devel
%if %{with java_sun}
BuildRequires:	java-sun-jre
BuildRequires:	jpackage-utils
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The IcedTea project provides a harness to build the source code from
http://openjdk.java.net/ using Free Software build tools and provides
replacements libraries for the binary plugs with code from the GNU
Classpath project.

%description -l pl.UTF-8
Projekt IcedTea daje możliwość kompilacji kodu źródłowego z
http://openjdk.java.net/ przy użyciu wolnodostępnych narzędzi oraz
dostarcza zamienniki biblioteczne binarnych wtyczek pochodzące z
projektu GNU Classpath.

%prep
%setup -q

find . -name '*.gmk' -exec sed -i -e 's#^PRINTF.*=.*#PRINTF = /bin/printf#g' "{}" ";"

%build
unset JAVA_HOME || :
%configure \
	--with-ecj-jar=%{_javadir}/ecj.jar \
	--with-libgcj-jar=%{_javadir}/libgcj.jar \
	--with-xalan2-jar=%{_javadir}/xalan.jar \
	--with-xalan2-serializer-jar=%{_javadir}/serializer.jar \
	--with-xerces2-jar=%{_javadir}/xerces.jar \
	--with-openjdk-src-zip=%{SOURCE1} \
	--with-openjdk-src=${PWD}/openjdk

%{__make} -j1 \
	%{?with_java_sun:BOOTDIR=%{java_home}} \
	SHELL=/bin/bash

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
