Summary:	Low level 3D scene-graph based graphics programming API for the Java language
Summary(pl):	Niskopoziomowe API programowania trójwymiarowych scen dla Javy
Name:		java3d
Version:	1.3.2
Release:	1
License:	Sun Binary Code License (restricted, non-distributable)
Group:		Libraries
# Download URL: https://java3d.dev.java.net/binary-builds.html
Source0:	http://download.java.net/media/java3d/builds/release/1.3.2/java3d-1_3_2-linux-i586.zip
# NoSource0-md5:	0d959d0be83eb60c9c135ae809caefb2
Source1:	http://download.java.net/media/java3d/builds/release/1.3.2/java3d-1_3_2-linux-amd64.zip
# NoSource1-md5:	bf2f39d332299f2aceb43cbad9a70428
Source2:	http://download.java.net/media/java3d/builds/release/1.3.2/java3d-1_3_2-doc.tar.gz
# NoSource2-md5:	9466da51587a0fc104b8243db100382e
NoSource:	0
NoSource:	1
NoSource:	2
URL:		https://java3d.dev.java.net/
Requires:	OpenGL >= 1.2
Requires:	OpenGL-GLX >= 1.3
Requires:	jre >= 1.4.2
ExclusiveArch:	%{ix86} %{x8664}
ExcludeArch:	i386 i486
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low level 3D scene-graph based graphics programming API for the Java
language.

%description -l pl
Niskopoziomowe API programowania trójwymiarowych scen dla Javy.

%package doc
Summary:	Java3D documentation
Summary(pl):	Dokumentacja biblioteki Java3D
Group:		Documentation

%description doc
Java3D documentation.

%description doc -l pl
Dokumentacja biblioteki Java3D.

%prep
%ifarch %{ix86}
%setup -q -n java3d-1_3_2-linux-i586 -a2
%endif
%ifarch %{x8664}
%setup -q -n java3d-1_3_2-linux-amd64 -T -b1 -a2
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/java/jre

%ifarch %{ix86}
unzip j3d-132-linux-x86.zip -d $RPM_BUILD_ROOT%{_libdir}/java/jre
%endif
%ifarch %{x8664}
unzip j3d-132-linux-amd64.zip -d $RPM_BUILD_ROOT%{_libdir}/java/jre
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BINARY-CODE-LICENSE.txt COPYRIGHT.txt RELEASE-NOTES.html
%ifarch %{ix86}
%attr(755,root,root) %{_libdir}/java/jre/lib/i386/lib*.so
%endif
%ifarch %{x8664}
%attr(755,root,root) %{_libdir}/java/jre/lib/amd64/lib*.so
%endif
%{_libdir}/java/jre/lib/ext/*.jar

%files doc
%defattr(644,root,root,755)
%doc java3d-1_3_2-doc/*
