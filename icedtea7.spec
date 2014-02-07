# TODO:
# - install .ttf fonts (same as in sun-java-base-jre-X11 package) or configure
#   it to use system fonts (is it possible?).

%bcond_with bootstrap   # build a bootstrap version, using icedtea6
%bcond_without nss	# don't use NSS
%bcond_without cacerts	# don't include the default CA certificates

%if %{with bootstrap}
%define		use_jdk	icedtea6
%else
%define		use_jdk	icedtea7
%endif

# class data version seen with file(1) that this jvm is able to load
%define		_classdataversion 51.0
# JDK/JRE version, as returned with `java -version`, '_' replaced with '.'
%define		_jdkversion 1.7.0.17

# hardcoded in Makefile.am
%define corba_changeset 3594dbde270d
%define jaxp_changeset 8fe156ad49e2
%define jaxws_changeset 32ea8b1ed91a
%define jdk_changeset 9db88c18e114
%define langtools_changeset dabd37b7e295
%define openjdk_changeset 410eb7fef869
%define cacao_version e215e36be9fc
%define jamvm_version ac22c9948434e528ece451642b4ebde40953ee7e

# defined in 'hostpot.map'
%define hotspot_changeset 2cb58882dac3

Summary:	OpenJDK and GNU Classpath code
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath
Name:		icedtea7
Version:	2.4.5
Release:	1
License:	GPL v2
Group:		Development/Languages/Java
Source0:	http://icedtea.wildebeest.org/download/source/icedtea-%{version}.tar.gz
# Source0-md5:	6dcc544657ade213d01017354a6f9858
Source1:	http://icedtea.wildebeest.org/hg/release/icedtea7-forest-2.4/archive/%{openjdk_changeset}.tar.gz
# Source1-md5:	09b9db8ca0b833070326573c3dac56e2
Source2:	http://icedtea.classpath.org/hg/release/icedtea7-forest-2.4/corba/archive/%{corba_changeset}.tar.gz
# Source2-md5:	adf888756629bdcb37f71451269ac42e
Source3:	http://icedtea.classpath.org/hg/release/icedtea7-forest-2.4/jaxp/archive/%{jaxp_changeset}.tar.gz
# Source3-md5:	1c42344779d49baed24724535a7e2c9b
Source4:	http://icedtea.classpath.org/hg/release/icedtea7-forest-2.4/jaxws/archive/%{jaxws_changeset}.tar.gz
# Source4-md5:	256148d7e7f5619addde91fd14bc3361
Source5:	http://icedtea.classpath.org/hg/release/icedtea7-forest-2.4/jdk/archive/%{jdk_changeset}.tar.gz
# Source5-md5:	3370074398071b4104e0e89efc9a4a56
Source6:	http://icedtea.classpath.org/hg/release/icedtea7-forest-2.4/langtools/archive/%{langtools_changeset}.tar.gz
# Source6-md5:	7605555236ffd8ac6bdedc6bc9b61c26
Source7:	http://icedtea.classpath.org/hg/release/icedtea7-forest-2.4/hotspot/archive/%{hotspot_changeset}.tar.gz
# Source7-md5:	67bb16313215e6da72bda7dc0090bb6a
Source10:	make-cacerts.sh
# patches for the IcedTea files
Patch0:		%{name}-i486.patch
Patch1:		%{name}-never_test_gamma.patch
# patches applied to the extracted sources
Patch100:	%{name}-libpath.patch
URL:		http://icedtea.classpath.org/wiki/Main_Page
BuildRequires:	alsa-lib-devel
BuildRequires:	ant
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bash
%{?with_cacerts:BuildRequires:	ca-certificates-update}
BuildRequires:	cups-devel
BuildRequires:	/usr/bin/jar
BuildRequires:	freetype-devel >= 2.3
BuildRequires:	gawk
BuildRequires:	giflib-devel
BuildRequires:	glib2-devel
BuildRequires:	glibc-misc
BuildRequires:	gtk+2-devel
BuildRequires:	heimdal-devel
BuildRequires:	java-rhino
BuildRequires:	java-xalan
%buildrequires_jdk
BuildRequires:	lcms2-devel
BuildRequires:	libffi-devel
# for /usr/share/java/ecj.jar:
BuildRequires:	libgcj
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libstdc++-static
BuildRequires:	lsb-release
%{?with_nss:BuildRequires:	nss-devel}
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.557
BuildRequires:	unzip
BuildRequires:	util-linux
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-proto-printproto-devel
BuildRequires:	xorg-proto-xproto-devel
BuildRequires:	zip
BuildRequires:	zlib-devel
Requires:	%{name}-appletviewer = %{version}-%{release}
Requires:	%{name}-jdk = %{version}-%{release}
Suggests:	%{name}-jre-X11
Suggests:	icedtea-web
Obsoletes:	icedtea6
Obsoletes:	java5-sun
Obsoletes:	java5-sun-jre
Obsoletes:	java5-sun-jre-jdbc
Obsoletes:	java5-sun-jre-X11
Obsoletes:	java5-sun-tools
Obsoletes:	java-gcj-compat
Obsoletes:	java-gcj-compat-devel
Obsoletes:	java-sun
Obsoletes:	java-sun-demos
Obsoletes:	java-sun-jre
Obsoletes:	java-sun-jre-alsa
Obsoletes:	java-sun-jre-jdbc
Obsoletes:	java-sun-jre-X11
Obsoletes:	java-sun-tools
Obsoletes:	oracle-java7
Obsoletes:	oracle-java7-jre
Obsoletes:	oracle-java7-jre-alsa
Obsoletes:	oracle-java7-jre-jdbc
Obsoletes:	oracle-java7-jre-X11
Obsoletes:	oracle-java7-tools
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dstreldir	%{name}-%{version}
%define		dstdir		%{_jvmdir}/%{dstreldir}
%define		jrereldir	%{dstreldir}/jre
%define		jredir		%{_jvmdir}/%{jrereldir}
%define		jvmjardir	%{_jvmjardir}/%{name}-%{version}

%ifarch %{x8664}
%define		jre_arch	amd64
%else
%define		jre_arch	i386
%endif

# to break artificial subpackage dependency loops
%define		_noautoreq	'libmawt.so' java\\\\(ClassDataVersion\\\\)

%description
The IcedTea project provides a harness to build the source code from
http://openjdk.java.net/ using Free Software build tools and provides
replacements libraries for the binary plugs with code from the GNU
Classpath project.

This is a meta-package which provides, by its dependencies, all the
IcedTea6 components including the OpenJDK, Java 6 developement kit and
runtime environment.

%description -l pl.UTF-8
Projekt IcedTea daje możliwość kompilacji kodu źródłowego z
http://openjdk.java.net/ przy użyciu wolnodostępnych narzędzi oraz
dostarcza zamienniki biblioteczne binarnych wtyczek pochodzące z
projektu GNU Classpath.

To jest meta-pakiet, który, za pośrednictwem zależności, dostarcza
wszystkie komponenty IcedTea6, w tym środowisko programistyczne
(OpenJDK) i uruchomieniowe (JRE).

%package jdk
Summary:	OpenJDK and GNU Classpath code - software development kit
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko programistyczne
Group:		Development/Languages/Java
Requires:	%{name}-jar = %{version}-%{release}
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre = %{version}-%{release}
Provides:	j2sdk = %{_jdkversion}
Provides:	jdk = %{_jdkversion}
Obsoletes:	blackdown-java-sdk
Obsoletes:	ibm-java
Obsoletes:	icedtea6-jdk
Obsoletes:	java-blackdown
Obsoletes:	java-gcj-compat-devel
Obsoletes:	java-sun
Obsoletes:	java5-sun
Obsoletes:	oracle-java7
Obsoletes:	jdk
Obsoletes:	kaffe

%description jdk
This package symlinks OpenJDK development tools provided by
%{name}-jdk-base to system-wide directories like %{_bindir}, making
IcedTea6 default JDK.

%description jdk -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do narzędzi programistycznych
OpenJDK, dostarczanych przez pakiet %{name}-jdk-base, w standardowych
systemowych ścieżkach takich jak %{_bindir}, sprawiając tym samym, że
IcedTea6 staje się domyślnym JDK w systemie.

%package jdk-base
Summary:	OpenJDK and GNU Classpath code - software development kit
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko programistyczne
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	jpackage-utils >= 0:1.7.5-4
Provides:	jdk(%{name})

%description jdk-base
OpenJDK development tools built using free software only.

%description jdk-base -l pl.UTF-8
OpenJDK skompilowane wyłącznie przy użyciu wolnego oprogramowania.

%package jre
Summary:	OpenJDK and GNU Classpath code - runtime environment
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko uruchomieniowe
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Provides:	java
Provides:	java(ClassDataVersion) = %{_classdataversion}
Provides:	java(jaas) = %{version}
Provides:	java(jaf) = 1.1.1
Provides:	java(jaxp) = 1.3
Provides:	java(jaxp_parser_impl)
Provides:	java(jce) = %{version}
Provides:	java(jdbc-stdext) = %{version}
Provides:	java(jdbc-stdext) = 3.0
Provides:	java(jmx) = 1.4
Provides:	java(jndi) = %{version}
Provides:	java(jsse) = %{version}
Provides:	java1.4
Provides:	jre = %{_jdkversion}
Obsoletes:	icedtea6-jre
Obsoletes:	java(jaas)
Obsoletes:	java(jaf)
Obsoletes:	java(jaxp)
Obsoletes:	java(jce)
Obsoletes:	java(jdbc-stdext)
Obsoletes:	java(jdbc-stdext)
Obsoletes:	java(jmx)
Obsoletes:	java(jndi)
Obsoletes:	java(jsse)
Obsoletes:	java-gcj-compat
Obsoletes:	java-sun-jre
Obsoletes:	java5-sun-jre
Obsoletes:	oracle-java7-jre
Obsoletes:	jre

%description jre
This package symlinks OpenJDK runtime environment tools provided by
%{name}-jre-base to system-wide directories like %{_bindir}, making
IcedTea6 default JRE.

%description jre -l pl.UTF-8
Ten pakiet tworzy symboliczne dowiązania do środowiska
uruchomieniowego OpenJDK, dostarczanych przez pakiet %{name}-jre-base,
w standardowych systemowych ścieżkach takich jak %{_bindir},
sprawiając tym samym, że IcedTea6 staje się domyślnym JRE w systemie.

%package jre-X11
Summary:	IcedTea6 OpenJDK - runtime environment - X11 support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa X11
Group:		Development/Languages/Java
Requires:	%{name}-jre = %{version}-%{release}
Requires:	%{name}-jre-base-X11 = %{version}-%{release}
Provides:	jre-X11 = %{_jdkversion}
Obsoletes:	icedtea6-jre-X11
Obsoletes:	java-sun-jre-X11
Obsoletes:	oracle-java7-jre-X11

%description jre-X11
X11 support for OpenJDK runtime environment built using free software
only.

%description jre-X11 -l pl.UTF-8
Biblioteki X11 dla środowiska OpenJDK zbudowany wyłocznie przy uzyciu
wolnego oprogramowania.

%package jre-base
Summary:	OpenJDK and GNU Classpath code - runtime environment
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - środowisko uruchomieniowe
Group:		Development/Languages/Java
Requires:	jpackage-utils >= 0:1.7.5-4
Provides:	jre(%{name})

%description jre-base
OpenJDK runtime environment built using free software only.

%description jre-base -l pl.UTF-8
Środowisko uruchomieniowe OpenJDK zbudowany wyłącznie przy użyciu
wolnego oprogramowania.

%package jre-base-X11
Summary:	IcedTea6 OpenJDK - runtime environment - X11 support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa X11
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}
Requires:	%{name}-jre-base-freetype = %{version}-%{release}

%description jre-base-X11
X11 support for OpenJDK runtime environment built using free software
only.

%description jre-base-X11 -l pl.UTF-8
Biblioteki X11 dla środowiska OpenJDK zbudowany wyłocznie przy uzyciu
wolnego oprogramowania.

%package jre-base-alsa
Summary:	IcedTea6 OpenJDK - runtime environment - ALSA support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa ALSA
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-base-alsa
ALSA sound support for OpenJDK runtime environment build using free
software only.

%description jre-base-alsa -l pl.UTF-8
Biblioteki ALSA rozszerzające środowisko OpenJDK o obsługę dźwięku
zbudowane przy uzyciu wyłącznie wolnego oprogramowania.

%package jre-base-freetype
Summary:	IcedTea6 OpenJDK - runtime environment - font support
Summary(pl.UTF-8):	IcedTea6 OpenJDK - środowisko uruchomieniowe - obsługa fontów
Group:		Development/Languages/Java
Requires:	%{name}-jre-base = %{version}-%{release}

%description jre-base-freetype
Font handling library for OpenJDK runtime environment built using free
software only.

%description jre-base-freetype -l pl.UTF-8
Biblioteki obsługi czcionek dla OpenJDK zbudowane wyłącznie przy
użyciu wolnego oprogramowania.

%package jar
Summary:	OpenJDK and GNU Classpath code - JAR tool
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - narzędzie JAR
Group:		Development/Languages/Java
Requires:	%{name}-jdk-base = %{version}-%{release}
Provides:	jar
Obsoletes:	fastjar
Obsoletes:	icedtea6-jar
Obsoletes:	jar

%description jar
JAR tool from OpenJDK built using free software only.

JAR is an archiver used to merge Java classes into a single library.

%description jar -l pl.UTF-8
Narzędzie jar z OpenJDK zbudowane przy uzyciu wyłącznie wolnego
oprogramowania.

JAR jest narzędziem pozwalającym wykonywać podstawowe operacje na
archiwach javy .jar takie jak na przykład tworzenie lub rozpakowywanie
archiwów.

%package appletviewer
Summary:	OpenJDK and GNU Classpath code - appletviewer tool
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - narzędzie appletviewer
Group:		Development/Languages/Java
Requires:	%{name}-jdk-base = %{version}-%{release}
Requires:	%{name}-jre-X11 = %{version}-%{release}
Obsoletes:	icedtea6-appletviewer
Obsoletes:	java-sun-appletviewer
Obsoletes:	oracle-java7-appletviewer

%description appletviewer
Appletviewer from OpenJDK build using free software only.

%description appletviewer -l pl.UTF-8
Appletviewer pozwala uruchamiać aplety javy niezależnie od
przeglądarki www. Ten appletviewer pochodzi z zestawu narzędzi OpenJDK
i został zbudowany wyłącznie przy użyciu wolnego oprogramowania.

%package jdk-sources
Summary:	OpenJDK and GNU Classpath code - sources
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - kod źródłowy
Group:		Documentation

%description jdk-sources
Source code for the OpenJDK development kit and Java standard library.

%description jdk-sources -l pl.UTF-8
Kod źródłowy narzędzi programistycznych OpenJDK oraz standardowej
biblioteki Javy.

%package examples
Summary:	OpenJDK and GNU Classpath code - examples
Summary(pl.UTF-8):	Kod OpenJDK i GNU Classpath - przykłady
Group:		Documentation

%description examples
Code examples for OpenJDK.

%description examples -l pl.UTF-8
Przykłady dla OpenJDK.

%prep
%setup -qn icedtea-%{version}
%patch0 -p1
%patch1 -p1

# patches to applied to the extracted sources
install -d pld-patches
cp -p %{PATCH100} pld-patches

# let the build system extract the sources where it wants them
install -d drops
ln -s %{SOURCE1} openjdk.tar.gz
ln -s %{SOURCE2} corba.tar.gz
ln -s %{SOURCE3} jaxp.tar.gz
ln -s %{SOURCE4} jaxws.tar.gz
ln -s %{SOURCE5} jdk.tar.gz
ln -s %{SOURCE6} langtools.tar.gz
ln -s %{SOURCE7} hotspot.tar.gz

%build
# Make sure we have /proc mounted - otherwise idlc will fail later.
if [ ! -f /proc/self/stat ]; then
	echo "You need to have /proc mounted in order to build this package!"
	exit 1
fi

unset JAVA_HOME

mkdir build-bin
export PATH="$(pwd)/build-bin:$PATH"

# our /usr/bin/ant is quite broken and won't run properly
# in the bootstrap JDK environment prepared by IcedTea build process
cat >>build-bin/ant <<'EOF'
#!/bin/sh

exec java \
	-classpath /usr/share/java/ant-launcher.jar \
	-Dant.home=/usr/share/ant \
	-Dant.lib=/usr/share/ant/lib \
	org.apache.tools.ant.launch.Launcher \
	"$@"
EOF
chmod a+x build-bin/ant

%{__aclocal}
%{__autoconf}
%{__automake}

# NOTE: the weird '--disable-bootstrap' is how it is supposed to be
# http://icedtea.classpath.org/wiki/CommonIssues#IcedTea7_building_on_systems_with_JDK_5_or_JDK_6
%configure \
	WGET=%{_bindir}/wget \
	--with-jdk-home=%{java_home} \
	%{?with_bootstrap:--disable-bootstrap} \
	--%{!?with_nss:dis}%{?with_nss:en}able-nss \
	--with-rhino=%{_javadir}/js.jar

%{__make} extract \
	SHELL=/bin/bash \
	DISTRIBUTION_PATCHES="$(echo pld-patches/*.patch)"

# if dpkg-architecure is installed (like on carme) it will break the build
# unless we disable using it somehow. As patching is difficult here:
%{__sed} -i -e's/dpkg-architecture/dpkg-architecture__/' openjdk/*/make/common/shared/Platform.gmk

%{__make} -j1 \
	SHELL=/bin/bash \
	DISABLE_HOTSPOT_OS_VERSION_CHECK=ok \
	DISTRIBUTION_PATCHES="$(echo pld-patches/*.patch)" \
	PRINTF=/bin/printf \
	MAX_VM_MEMORY=1024

%{?with_cacerts:%{__sh} %{SOURCE10}}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{dstdir},%{_mandir}/ja} \
	$RPM_BUILD_ROOT{%{jvmjardir},%{_examplesdir}/%{name}-%{version},%{_javasrcdir}} \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}

# install the 'JDK image', it contains the JRE too
cp -a openjdk.build/j2sdk-image/* $RPM_BUILD_ROOT%{dstdir}

# convenience symlinks without version number
ln -s %{dstreldir} $RPM_BUILD_ROOT%{_jvmdir}/%{name}
ln -s %{jrereldir} $RPM_BUILD_ROOT%{_jvmdir}/%{name}-jre

ln -s %{dstreldir} $RPM_BUILD_ROOT%{_jvmdir}/java

# move JDK sources and demo to /usr/src
mv $RPM_BUILD_ROOT%{dstdir}/demo $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{dstdir}/sample $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
mv $RPM_BUILD_ROOT%{dstdir}/src.zip $RPM_BUILD_ROOT%{_javasrcdir}/%{name}-jdk.zip

# move manual pages to its place
mv $RPM_BUILD_ROOT%{dstdir}/man/ja_JP.UTF-8/man1 $RPM_BUILD_ROOT%{_mandir}/ja/man1
rmdir $RPM_BUILD_ROOT%{dstdir}/man/ja_JP.UTF-8
rm $RPM_BUILD_ROOT%{dstdir}/man/ja
mv $RPM_BUILD_ROOT%{dstdir}/man/man1 $RPM_BUILD_ROOT%{_mandir}/man1
rmdir $RPM_BUILD_ROOT%{dstdir}/man

# replace duplicates with symlinks, link to %{_bindir}
for path in $RPM_BUILD_ROOT%{dstdir}/bin/*; do
	filename=$(basename $path)
	if diff -q "$path" "$RPM_BUILD_ROOT%{jredir}/bin/$filename" > /dev/null; then
		ln -sf "../jre/bin/$filename" "$path"
		ln -sf "%{jredir}/bin/$filename" $RPM_BUILD_ROOT%{_bindir}
	else
		ln -sf "%{dstdir}/bin/$filename" $RPM_BUILD_ROOT%{_bindir}
	fi
done
ln -sf ../jre/lib/jexec $RPM_BUILD_ROOT%{dstdir}/lib/jexec

# keep configuration in /etc (not all *.properties go there)
for config in management security content-types.properties \
		logging.properties net.properties sound.properties; do

	mv $RPM_BUILD_ROOT%{jredir}/lib/$config $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/$config
	ln -s %{_sysconfdir}/%{name}/$config $RPM_BUILD_ROOT%{jredir}/lib/$config
done

ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jsse.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jcert.jar
ln -sf %{jredir}/lib/jsse.jar $RPM_BUILD_ROOT%{jvmjardir}/jnet.jar
ln -sf %{jredir}/lib/jce.jar $RPM_BUILD_ROOT%{jvmjardir}/jce.jar
for f in jndi jndi-ldap jndi-cos jndi-rmi jaas jdbc-stdext jdbc-stdext-3.0 \
	sasl jaxp_parser_impl jaxp_transform_impl jaxp jmx activation xml-commons-apis \
	jndi-dns jndi-rmi; do
	ln -sf %{jredir}/lib/rt.jar $RPM_BUILD_ROOT%{jvmjardir}/$f.jar
done

# some apps (like opera) looks for it in different place
ln -s server/libjvm.so $RPM_BUILD_ROOT%{jredir}/lib/%{jre_arch}/libjvm.so

%{__rm} $RPM_BUILD_ROOT%{dstdir}/{,jre/}{ASSEMBLY_EXCEPTION,LICENSE,THIRD_PARTY_README}

%{?with_cacerts:install cacerts $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/security}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING NEWS README

%files jdk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/apt
%attr(755,root,root) %{_bindir}/extcheck
%attr(755,root,root) %{_bindir}/idlj
%attr(755,root,root) %{_bindir}/jarsigner
%attr(755,root,root) %{_bindir}/java-rmi.cgi
%attr(755,root,root) %{_bindir}/javac
%attr(755,root,root) %{_bindir}/javadoc
%attr(755,root,root) %{_bindir}/javah
%attr(755,root,root) %{_bindir}/javap
%attr(755,root,root) %{_bindir}/jcmd
%attr(755,root,root) %{_bindir}/jconsole
%attr(755,root,root) %{_bindir}/jdb
%attr(755,root,root) %{_bindir}/jhat
%attr(755,root,root) %{_bindir}/jinfo
%attr(755,root,root) %{_bindir}/jmap
%attr(755,root,root) %{_bindir}/jps
%attr(755,root,root) %{_bindir}/jrunscript
%attr(755,root,root) %{_bindir}/jsadebugd
%attr(755,root,root) %{_bindir}/jstack
%attr(755,root,root) %{_bindir}/jstat
%attr(755,root,root) %{_bindir}/jstatd
%attr(755,root,root) %{_bindir}/native2ascii
%attr(755,root,root) %{_bindir}/rmic
%attr(755,root,root) %{_bindir}/schemagen
%attr(755,root,root) %{_bindir}/serialver
%attr(755,root,root) %{_bindir}/wsgen
%attr(755,root,root) %{_bindir}/wsimport
%attr(755,root,root) %{_bindir}/xjc
%{_jvmdir}/java
%{_mandir}/man1/apt.1*
%{_mandir}/man1/extcheck.1*
%{_mandir}/man1/idlj.1*
%{_mandir}/man1/jarsigner.1*
%{_mandir}/man1/javac.1*
%{_mandir}/man1/javadoc.1*
%{_mandir}/man1/javah.1*
%{_mandir}/man1/javap.1*
%{_mandir}/man1/jcmd.1*
%{_mandir}/man1/jconsole.1*
%{_mandir}/man1/jdb.1*
%{_mandir}/man1/jhat.1*
%{_mandir}/man1/jinfo.1*
%{_mandir}/man1/jmap.1*
%{_mandir}/man1/jps.1*
%{_mandir}/man1/jrunscript.1*
%{_mandir}/man1/jsadebugd.1*
%{_mandir}/man1/jstack.1*
%{_mandir}/man1/jstat.1*
%{_mandir}/man1/jstatd.1*
%{_mandir}/man1/native2ascii.1*
%{_mandir}/man1/schemagen.1*
%{_mandir}/man1/serialver.1*
%{_mandir}/man1/rmic.1*
%{_mandir}/man1/wsgen.1*
%{_mandir}/man1/wsimport.1*
%{_mandir}/man1/xjc.1*
%lang(ja) %{_mandir}/ja/man1/apt.1*
%lang(ja) %{_mandir}/ja/man1/extcheck.1*
%lang(ja) %{_mandir}/ja/man1/idlj.1*
%lang(ja) %{_mandir}/ja/man1/jarsigner.1*
%lang(ja) %{_mandir}/ja/man1/javac.1*
%lang(ja) %{_mandir}/ja/man1/javadoc.1*
%lang(ja) %{_mandir}/ja/man1/javah.1*
%lang(ja) %{_mandir}/ja/man1/javap.1*
%lang(ja) %{_mandir}/ja/man1/jcmd.1*
%lang(ja) %{_mandir}/ja/man1/jconsole.1*
%lang(ja) %{_mandir}/ja/man1/jdb.1*
%lang(ja) %{_mandir}/ja/man1/jhat.1*
%lang(ja) %{_mandir}/ja/man1/jinfo.1*
%lang(ja) %{_mandir}/ja/man1/jmap.1*
%lang(ja) %{_mandir}/ja/man1/jps.1*
%lang(ja) %{_mandir}/ja/man1/jrunscript.1*
%lang(ja) %{_mandir}/ja/man1/jsadebugd.1*
%lang(ja) %{_mandir}/ja/man1/jstack.1*
%lang(ja) %{_mandir}/ja/man1/jstat.1*
%lang(ja) %{_mandir}/ja/man1/jstatd.1*
%lang(ja) %{_mandir}/ja/man1/native2ascii.1*
%lang(ja) %{_mandir}/ja/man1/schemagen.1*
%lang(ja) %{_mandir}/ja/man1/serialver.1*
%lang(ja) %{_mandir}/ja/man1/rmic.1*
%lang(ja) %{_mandir}/ja/man1/wsgen.1*
%lang(ja) %{_mandir}/ja/man1/wsimport.1*
%lang(ja) %{_mandir}/ja/man1/xjc.1*

%files jdk-base
%defattr(644,root,root,755)
%doc openjdk.build/j2sdk-image/THIRD_PARTY_README
%doc openjdk.build/j2sdk-image/ASSEMBLY_EXCEPTION
%dir %{dstdir}
%{_jvmdir}/%{name}
%attr(755,root,root) %{dstdir}/bin/appletviewer
%attr(755,root,root) %{dstdir}/bin/apt
%attr(755,root,root) %{dstdir}/bin/extcheck
%attr(755,root,root) %{dstdir}/bin/idlj
%attr(755,root,root) %{dstdir}/bin/jar
%attr(755,root,root) %{dstdir}/bin/jarsigner
%attr(755,root,root) %{dstdir}/bin/java-rmi.cgi
%attr(755,root,root) %{dstdir}/bin/javac
%attr(755,root,root) %{dstdir}/bin/javadoc
%attr(755,root,root) %{dstdir}/bin/javah
%attr(755,root,root) %{dstdir}/bin/javap
%attr(755,root,root) %{dstdir}/bin/jconsole
%attr(755,root,root) %{dstdir}/bin/jcmd
%attr(755,root,root) %{dstdir}/bin/jdb
%attr(755,root,root) %{dstdir}/bin/jhat
%attr(755,root,root) %{dstdir}/bin/jinfo
%attr(755,root,root) %{dstdir}/bin/jmap
%attr(755,root,root) %{dstdir}/bin/jps
%attr(755,root,root) %{dstdir}/bin/jrunscript
%attr(755,root,root) %{dstdir}/bin/jsadebugd
%attr(755,root,root) %{dstdir}/bin/jstack
%attr(755,root,root) %{dstdir}/bin/jstat
%attr(755,root,root) %{dstdir}/bin/jstatd
%attr(755,root,root) %{dstdir}/bin/native2ascii
%attr(755,root,root) %{dstdir}/bin/rmic
%attr(755,root,root) %{dstdir}/bin/schemagen
%attr(755,root,root) %{dstdir}/bin/serialver
%attr(755,root,root) %{dstdir}/bin/wsgen
%attr(755,root,root) %{dstdir}/bin/wsimport
%attr(755,root,root) %{dstdir}/bin/xjc
%{dstdir}/include
%dir %{dstdir}/lib
%{dstdir}/lib/ct.sym
%{dstdir}/lib/dt.jar
%{dstdir}/lib/ir.idl
%{dstdir}/lib/jconsole.jar
%attr(755,root,root) %{dstdir}/lib/jexec
%{dstdir}/lib/orb.idl
%ifnarch i486
%{dstdir}/lib/sa-jdi.jar
%endif
%{dstdir}/lib/tools.jar
%dir %{dstdir}/lib/%{jre_arch}
%dir %{dstdir}/lib/%{jre_arch}/jli
%attr(755,root,root) %{dstdir}/lib/%{jre_arch}/jli/*.so
%{dstdir}/tapset

%files jre
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/java
%attr(755,root,root) %{_bindir}/keytool
%attr(755,root,root) %{_bindir}/orbd
%attr(755,root,root) %{_bindir}/pack200
%attr(755,root,root) %{_bindir}/rmid
%attr(755,root,root) %{_bindir}/rmiregistry
%attr(755,root,root) %{_bindir}/servertool
%attr(755,root,root) %{_bindir}/tnameserv
%attr(755,root,root) %{_bindir}/unpack200
%{_mandir}/man1/java.1*
%{_mandir}/man1/keytool.1*
%{_mandir}/man1/orbd.1*
%{_mandir}/man1/pack200.1*
%{_mandir}/man1/rmid.1*
%{_mandir}/man1/rmiregistry.1*
%{_mandir}/man1/servertool.1*
%{_mandir}/man1/tnameserv.1*
%{_mandir}/man1/unpack200.1*
%lang(ja) %{_mandir}/ja/man1/java.1*
%lang(ja) %{_mandir}/ja/man1/keytool.1*
%lang(ja) %{_mandir}/ja/man1/orbd.1*
%lang(ja) %{_mandir}/ja/man1/pack200.1*
%lang(ja) %{_mandir}/ja/man1/rmid.1*
%lang(ja) %{_mandir}/ja/man1/rmiregistry.1*
%lang(ja) %{_mandir}/ja/man1/servertool.1*
%lang(ja) %{_mandir}/ja/man1/tnameserv.1*
%lang(ja) %{_mandir}/ja/man1/unpack200.1*

%files jre-base
%defattr(644,root,root,755)
%doc openjdk.build/j2sdk-image/THIRD_PARTY_README
%doc openjdk.build/j2sdk-image/ASSEMBLY_EXCEPTION
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/%{name}/*
%dir %{dstdir}
%{dstdir}/release
%dir %{jredir}
%{_jvmdir}/%{name}-jre
%dir %{jredir}/bin
%dir %{dstdir}/bin
%attr(755,root,root) %{jredir}/bin/java
%attr(755,root,root) %{dstdir}/bin/java
%attr(755,root,root) %{jredir}/bin/keytool
%attr(755,root,root) %{dstdir}/bin/keytool
%attr(755,root,root) %{jredir}/bin/orbd
%attr(755,root,root) %{dstdir}/bin/orbd
%attr(755,root,root) %{jredir}/bin/pack200
%attr(755,root,root) %{dstdir}/bin/pack200
%attr(755,root,root) %{jredir}/bin/rmid
%attr(755,root,root) %{dstdir}/bin/rmid
%attr(755,root,root) %{jredir}/bin/rmiregistry
%attr(755,root,root) %{dstdir}/bin/rmiregistry
%attr(755,root,root) %{jredir}/bin/servertool
%attr(755,root,root) %{dstdir}/bin/servertool
%attr(755,root,root) %{jredir}/bin/tnameserv
%attr(755,root,root) %{dstdir}/bin/tnameserv
%attr(755,root,root) %{jredir}/bin/unpack200
%attr(755,root,root) %{dstdir}/bin/unpack200
%dir %{jredir}/lib
%dir %{jredir}/lib/applet
%{jredir}/lib/cmm
%{jredir}/lib/ext
%dir %{jredir}/lib/%{jre_arch}
%ifnarch %{x8664} i486
%dir %{jredir}/lib/%{jre_arch}/client
%{jredir}/lib/%{jre_arch}/client/Xusage.txt
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/client/*.so
%endif
%dir %{jredir}/lib/%{jre_arch}/headless
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/headless/*.so
%dir %{jredir}/lib/%{jre_arch}/jli
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/jli/*.so
%dir %{jredir}/lib/%{jre_arch}/server
%{jredir}/lib/%{jre_arch}/server/Xusage.txt
%ifnarch i486
%{jredir}/lib/%{jre_arch}/server/classes.jsa
%endif
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/server/*.so
%{jredir}/lib/%{jre_arch}/jvm.cfg
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libattach.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libawt.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libdt_socket.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libhprof.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libinstrument.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libj2gss.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libj2krb5.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libj2pcsc.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libj2pkcs11.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjaas_unix.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjava.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjavajpeg.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjavalcms.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjava_crw_demo.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjawt.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjdwp.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjsdt.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjsig.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjsound.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjvm.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libmanagement.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libmlib_image.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libnet.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libnio.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libnpt.so
%ifnarch i486
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libsaproc.so
%endif
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libsctp.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libunpack.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libverify.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libzip.so
%{jredir}/lib/images
%{jredir}/lib/management
%{jredir}/lib/security
%{jredir}/lib/zi
#
%if %{with webstart}
%{jredir}/lib/about.jar
%{jredir}/lib/about.jnlp
%endif
%{jredir}/lib/calendars.properties
%{jredir}/lib/charsets.jar
%{jredir}/lib/classlist
%{jredir}/lib/content-types.properties
%{jredir}/lib/currency.data
%{jredir}/lib/flavormap.properties
%{jredir}/lib/fontconfig.*
%{jredir}/lib/jce.jar
%attr(755, root, root) %{jredir}/lib/jexec
%{jredir}/lib/jsse.jar
%{jredir}/lib/jvm.hprof.txt
%{jredir}/lib/logging.properties
%{jredir}/lib/management-agent.jar
%{jredir}/lib/meta-index
%{jredir}/lib/net.properties
%{jredir}/lib/psfont.properties.ja
%{jredir}/lib/psfontj2d.properties
%{jredir}/lib/resources.jar
%{jredir}/lib/rhino.jar
%{jredir}/lib/rt.jar
%{jredir}/lib/sound.properties
%{jredir}/lib/tz.properties
%{jvmjardir}

%files jre-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/policytool
%{_mandir}/man1/policytool.1*
%lang(ja) %{_mandir}/ja/man1/policytool.1*

%files jre-base-X11
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/bin/policytool
%attr(755,root,root) %{dstdir}/bin/policytool
%dir %{jredir}/lib/%{jre_arch}/xawt
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/xawt/*.so
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libsplashscreen.so

%files jre-base-alsa
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libjsoundalsa.so

%files jre-base-freetype
%defattr(644,root,root,755)
%attr(755,root,root) %{jredir}/lib/%{jre_arch}/libfontmanager.so

%files jar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/jar
%{_mandir}/man1/jar.1*
%lang(ja) %{_mandir}/ja/man1/jar.1*

%files appletviewer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/appletviewer
%{_mandir}/man1/appletviewer.1*
%lang(ja) %{_mandir}/ja/man1/appletviewer.1*

%files jdk-sources
%defattr(644,root,root,755)
%{_javasrcdir}/%{name}-jdk.zip

%files examples
%defattr(644,root,root,755)
%{_examplesdir}/%{name}-%{version}
