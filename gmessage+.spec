Summary:	display a message (like xmessage)
Name:		gmessage+
Version:	0.17
Release:	2
License:	GPL
Group:		X11/Applications/Networking
Group(de):	X11/Applikationen/Netzwerkwesen
Group(pl):	X11/Aplikacje/Sieciowe
Source0:	http://ymettier.free.fr/gmsgp/download/%{name}-%{version}.tar.gz
URL:		http://ymettier.free.fr/gmsgp/gmsgp.html
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gmessage+ is a clone of xmessage. I is used to display a message box
with a text specified on the command line, a file or via a pipe.

%description -l pl
gmessage+ jest klonem xmessage. Mozna go wykorzysta� do wy�wietlania
okienek z tekstem przy pomocy lini komend z linii polece�, pliku lub
potoku.

%description -l fr
gmessage+ est un clone de xmessage. Il permet d'afficher un message
dans une boite de dialogue. Ce message est sp�cifi� via la ligne de
commande, un fichier ou un pipe.

%prep
%setup -q

%build
gettextize --copy --force
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README NEWS AUTHORS ChangeLog TODO

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
