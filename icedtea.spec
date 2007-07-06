# TODO:
# - fix bash substitution
#
%bcond_without	bootstrap	# don't perform bootstrap build
#
%define	snap	20070626
Summary:	OpenJDK and GNU Classpath code
SummarY(pl.UTF-8):	Kod OpenJDK i GNU Classpath
Name:		icedtea
Version:	1.0
Release:	0.%{snap}.1
License:	GPL
Group:		Development/Languages/Java
Source0:	%{name}-%{snap}.tar.gz
# Source0-md5:	8a7d2c92662b06c31dc4ada65004a508
Source1:	http://download.java.net/openjdk/jdk7/promoted/b14/openjdk-7-ea-src-b14-21_jun_2007.zip
# Source1-md5:	c126a32966e4bdb6a60a5724d9447966
URL:		http://icedtea.classpath.org/wiki/Main_Page
BuildRequires:	bash
BuildRequires:	cups-devel
BuildRequires:	eclipse-ecj
BuildRequires:	findutils
BuildRequires:	jdk
BuildRequires:	libgcj
BuildRequires:	libstdc++-devel
BuildRequires:	motif-devel
BuildRequires:	unzip
BuildRequires:	xalan-j
BuildRequires:	xerces-j
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-xproto-devel
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
%setup -q -n %{name} -a1

sed -i -e 's#-Werror##g' openjdk/hotspot/build/linux/makefiles/gcc.make openjdk/j2se/make/common/*.gmk

%build
%configure \
	--with-ecj-jar=%{_javadir}/ecj.jar \
	--with-libgcj-jar=%{_javadir}/libgcj.jar \
	--with-xalan2-jar=%{_javadir}/xalan.jar \
	--with-xalan2-serializer-jar=%{_javadir}/serializer.jar \
	--with-xerces2-jar=%{_javadir}/xerces.jar \
	--with-openjdk-src-zip=%{SOURCE1} \
	--with-openjdk-src=${PWD}/openjdk

%{__make} -j1 %{?with_bootstrap:bootstrap} \
	SHELL=/bin/bash \
	BOOTDIR=%{java_home}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
