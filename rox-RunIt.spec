%define _name RunIt
Summary:	ROX-RunIt executes a single command
Summary(pl.UTF-8):	ROX-RunIt wykonuje pojedynczą komendę
Name:		rox-%{_name}
Version:	0.9.5
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	http://metabocks.port5.com/rox/runit.tar.gz
# Source0-md5:	b56240a8a9d85ffa35535abf3eb659df
URL:		http://www.metabocks.com/rox/
Requires:	python-pygtk-gtk
Requires:	rox-Lib
%pyrequires_eq	python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appsdir	%{_libdir}/ROX-apps

%description
ROX-RunIt is a very simple application which was inspired by GNOME's
Minicommander. Basically it executes a single command. In applet mode
it creates a small window that sits on the ROX panel where you can
type a command.

%description -l pl.UTF-8
ROX-RunIt jest bardzo prostą aplikacją zainspirowaną przez GNOME
Minicomandera. Program ten po prostu wykonuje pojedynczą komendę. Jako
aplet, tworzy on małe okienko na panelu ROXa, w którym możesz wpisywać
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
