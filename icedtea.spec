# TODO:
# - fix bash substitution
#
Summary:	OpenJDK and GNU Classpath code
SummarY(pl.UTF-8):	Kod OpenJDK i GNU Classpath
Name:		icedtea
Version:	1.8
Release:	0.1
License:	GPL
Group:		Development/Languages/Java
Source0:	http://icedtea.classpath.org/download/source/%{name}-%{version}.tar.gz
# Source0-md5:	b165d877e0f9824a2b492541be945874
# Create this one by running make dist-openjdk (needs mercurial + mercurial forest extension)
Source1:	openjdk-b26.zip
# Source1-md5:	7a5d2da503fde6ba09df9773d7df27ca
URL:		http://icedtea.classpath.org/wiki/Main_Page
BuildRequires:	alsa-lib-devel
BuildRequires:	bash
BuildRequires:	cups-devel
BuildRequires:	eclipse-ecj
BuildRequires:	freetype-devel >= 2.3
BuildRequires:	gcc-java >= 6:4.3
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gdk-pixbuf-devel
BuildRequires:	jdk
BuildRequires:	libgcj
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-devel
BuildRequires:	motif-devel
BuildRequires:	rhino
BuildRequires:	unzip
BuildRequires:	xalan-j
BuildRequires:	xerces-j
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	xulrunner-devel
BuildRequires:	zlib-devel
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
# source1 should unpack itself into the same dir
# as specified in --with-openjdk-src=
%setup -q -a1

sed -i -e 's#^PRINTF.*=.*#PRINTF = /bin/printf#g' \
	openjdk/*/make/common/shared/Defs-utils.gmk

mv openjdk openjdk-src

%build
unset JAVA_HOME || :
%configure \
	--with-gcj-home=%{_prefix} \
	--with-ecj=%{_bindir}/ecj \
	--with-ecj-jar=%{_javadir}/ecj.jar \
	--with-libgcj-jar=%{_javadir}/libgcj.jar \
	--with-xalan2-jar=%{_javadir}/xalan.jar \
	--with-xalan2-serializer-jar=%{_javadir}/serializer.jar \
	--with-xerces2-jar=%{_javadir}/xerces.jar \
	--with-openjdk-src-dir=${PWD}/openjdk-src \
	--with-rhino=%{_javadir}/js.jar

%{__make} -j1 \
	SHELL=/bin/bash

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
