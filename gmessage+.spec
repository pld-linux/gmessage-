Summary:	Display a message (like xmessage)
Summary(pl.UTF-8):	Program wyświetlający komunikat (podobny do xmessage)
Name:		gmessage+
Version:	0.17
Release:	3
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://ymettier.free.fr/gmsgp/download/%{name}-%{version}.tar.gz
# Source0-md5:	d4af8279cb37d3ad9b0bc6b25259e6de
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


%description
gmessage+ is a clone of xmessage. I is used to display a message box
with a text specified on the command line, a file or via a pipe.

%description -l pl.UTF-8
gmessage+ jest klonem xmessage. Można go wykorzystać do wyświetlania
okienek z tekstem podanym z linii poleceń, pliku lub potoku.

%description -l fr.UTF-8
gmessage+ est un clone de xmessage. Il permet d'afficher un message
dans une boite de dialogue. Ce message est spécifié via la ligne de
commande, un fichier ou un pipe.

%prep
%setup -q
%patch -P0 -p1

%build
rm -f missing
%{__gettextize}
%{__libtoolize}
%{__aclocal}
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
