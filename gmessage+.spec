Summary:	display a message (like xmessage)
Name:		gmessage+
Version:	0.5
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://ymettier.free.fr/gmsgp/download/%{name}-%{version}.tar.gz
URL:		http://ymettier.free.fr/gmsgp/gmsgp.html
BuildRequires:	gettext-devel
BUildRequires:	esound-devel
BUildRequires:	gtk+-devel
BUildRequires:	imlib-devel
BUildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gmessage+ is a clone of xmessage. I is used to display a message box with a
text specified on the command line, a file or via a pipe.

%description -l fr
gmessage+ est un clone de xmessage. Il permet d'afficher un message dans une
boite de dialogue. Ce message est spécifié via la ligne de commande, un
fichier ou un pipe.

%prep
rm -rf $RPM_BUILD_ROOT

%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS AUTHORS ChangeLog TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/gmsgp
