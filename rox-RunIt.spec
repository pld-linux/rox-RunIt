%include  /usr/lib/rpm/macros.python
%define _appsdir /usr/X11R6/share/ROX-apps
%define _name RunIt
Summary:	ROX-RunIt executes a single command
Summary(pl):	ROX-RunIt wykonuje pojedyncz± komendê
Name:		rox-%{_name}
Version:	0.9.5
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.speakeasy.org/~pngwen/rox/runit.tar.gz
URL:		http://www.metabocks.com/rox
BuildRequires:	rpm-pythonprov
Requires:	python-pygtk
Requires:	rox-Lib
%pyrequires_eq  python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
ROX-RunIt is a very simple application which was inspired by Gnome's
Minicommander. Basically it executes a single command. In applet mode
it creates a small window that sits on the ROX panel where you can
type a command.

%description -l pl
ROX-RunIt jest bardzo prost± aplikacj± zainspirowan± przez Gnome
Minicomandera. Program ten po prostu wykonuje pojedyncz± komendê. Jako
aplet, tworzy on ma³e okienko na panelu ROXa, w którym mo¿esz wpisywaæ
komendy.

%prep
%setup -q -n %{_name}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

install App* *.py ErrorRun $RPM_BUILD_ROOT%{_appsdir}/%{_name}
install Help/README $RPM_BUILD_ROOT%{_appsdir}/%{_name}/Help

%py_comp $RPM_BUILD_ROOT%{_appsdir}/%{_name}
%py_ocomp $RPM_BUILD_ROOT%{_appsdir}/%{_name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_appsdir}/%{_name}/*Run
%attr(755,root,root) %{_appsdir}/%{_name}/app*.py
%{_appsdir}/%{_name}/AppI*
%{_appsdir}/%{_name}/findrox.py[co]
%{_appsdir}/%{_name}/runit.py[co]
%{_appsdir}/%{_name}/Help
%dir %{_appsdir}/%{_name}
