%define name gmessage+
%define version 0.5
%define release 1
Name: %{name}
Version: %{version}
Release: %{release}
Summary: display a message (like xmessage)
Source: %{name}-%{version}.tar.gz
URL: http://ymettier.free.fr/gmsgp/gmsgp.html
Group: Applications/System
BuildRoot: %{_tmppath}/%{name}-buildroot
Copyright: GPL
Prefix: %{_prefix}
Requires: gnome-libs

%description
gmessage+ is a clone of xmessage. I is used to display a message box with a text
specified on the command line, a file or via a pipe.

%description -l fr
gmessage+ est un clone de xmessage. Il permet d'afficher un message dans une
boite de dialogue. Ce message est spécifié via la ligne de commande, un fichier
ou un pipe.

%prep
rm -rf $RPM_BUILD_ROOT

%setup

%build
CFLAGS="$RPM_OPT_FLAGS" %configure --prefix=%prefix
make

%install
make install prefix=$RPM_BUILD_ROOT/%{prefix}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%doc README NEWS COPYING AUTHORS ChangeLog TODO
%{prefix}/bin/gmsgp
%{prefix}/share/*/*/*

%changelog
* Sat Apr 1 2000 Yves Mettier <ymettier@free.fr>
- First spec file (gmessage+ v0.5)
