Summary:	Low level 3D scene-graph based graphics programming API for the Java language
Summary(pl):	Niskopoziomowe API programowania trójwymiarowych scen dla Javy
Name:		java3d
Version:	1.3.1
Release:	1
License:	restricted, non-distributable
Group:		Libraries
Source0:	ftp://ftp.tux.org/pub/java/java3d/1.3.1/i386/fcs/%{name}-re-%{version}-linux-i386.bin
# NoSource0-md5:	c79557ec7da5fa7dac742c35fd721350
URL:		http://java.sun.com/products/java-media/3D/index.jsp 
Requires:	jre >= 1.4.1
# Other archs also supported, but I don't care.
ExclusiveArch:	%{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Low level 3D scene-graph based graphics programming API for the Java
language.

%description -l pl
Niskopoziomowe API programowania trójwymiarowych scen dla Javy.

%prep
%setup -q -c -T
install %{SOURCE0} .

%build
export MORE=10000
sh java3d-re-%{version}-linux-i386.bin << EOF
yes
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/java/jre/lib/{ext,i386}

install lib/ext/* $RPM_BUILD_ROOT%{_libdir}/java/jre/lib/ext
install lib/i386/* $RPM_BUILD_ROOT%{_libdir}/java/jre/lib/i386

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE-Java3D README-Java3D
%{_libdir}/java/jre/lib/ext/*
%{_libdir}/java/jre/lib/i386/*
