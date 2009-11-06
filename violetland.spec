Summary:	Opensource crossplatform game similar to crimsonland
Summary(pl.UTF-8):	Otwarta gra wieloplatformowa podobna do crimsonland
Name:		violetland
Version:	0.2.2
Release:	1
License:	GPL v3+
Group:		X11/Applications/Games
Source0:	http://violetland.googlecode.com/files/%{name}-v%{version}-src.zip
# Source0-md5:	933cc7f6be0e45ff39e67129c8e731c9
Patch0:		%{name}-useless_files.patch
URL:		http://code.google.com/p/violetland/
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	cmake
BuildRequires:	unzip
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In this game the player should help a girl by name of Violet to
struggle with hordes of monsters. For this purpose the various weapon,
and also the special abilities of the heroine which are opening with
experience can be used. In game there are elements of RPG in the form
of strength-agility-vitality and derivatives. Also there is an unique
feature: dynamic change of day and night.

%description -l pl.UTF-8
W grze zadaniem gracza jest pomoc dziewczynie o imieniu Violet w walce
z hordą potworów. Do tego celu posłuży nam róznego rodzaju broń,
specjalne właściwości heroiny oraz doświadczenie. W grze występują
elementy RPG w formie siła-zręczność-witalnośc oraz pochodne. Gra
posiada również unikalną cechę: dynamiczne zmiany dnia i nocy.

%prep
%setup -q -n %{name}-v%{version}
%patch0 -p1

%build
mkdir build && cd build
%cmake .. \
	-DCMAKE_INSTALL_PREFIX="%{_prefix}"
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

cd build
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/violetland
%{_datadir}/%{name}
