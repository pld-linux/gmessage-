Summary:	Display a message (like xmessage)
Summary(pl):	Program wy¶wietlaj±cy komunikat (podobny do xmessage)
Name:		gmessage+
Version:	0.17
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ymettier.free.fr/gmsgp/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_am.patch
URL:		http://ymettier.free.fr/gmsgp/gmsgp.html
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esound-devel
BuildRequires:	gettext-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gtk+-devel
BuildRequires:	imlib-devel
BuildRequires:	libtool
BuildRequires:	popt-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
gmessage+ is a clone of xmessage. I is used to display a message box
with a text specified on the command line, a file or via a pipe.

%description -l pl
gmessage+ jest klonem xmessage. Mozna go wykorzystaæ do wy¶wietlania
okienek z tekstem podanym z linii poleceñ, pliku lub potoku.

%description -l fr
gmessage+ est un clone de xmessage. Il permet d'afficher un message
dans une boite de dialogue. Ce message est spécifié via la ligne de
commande, un fichier ou un pipe.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__libtoolize}
aclocal
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README NEWS AUTHORS ChangeLog TODO
%attr(755,root,root) %{_bindir}/*
