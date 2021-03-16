Summary: Mk-livestatus is a Nagios Event Broker
Name: 	 mk-livestatus
Version: 1.2.8p17
Release: 0.rgm
License: GPL
Group: 	 Applications/System
URL: 	 http://mathias-kettner.de/

Source0: %{name}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

Requires: nagios >= 3.0

BuildRequires: gcc-c++

# nagios paths
%define linkdir		%{rgm_path}/%{name}
%define datadir 	%{linkdir}-%{version}
%define bindir 		%{datadir}/bin
%define libdir 		%{datadir}/lib

%description
Livestatus make use of the Nagios Event Broker API and loads a binary module into your Nagios process. But other then NDO, Livestatus does not actively write out data. Instead, it opens a socket by which data can be retrieved on demand. 

%prep
%setup -T -b 0 -n %{name}

%build
cd ../%{name}
%configure \
	--bindir="%{bindir}" \
	--libdir="%{bindir}" 
make GYPFLAGS="-Dclang=0"

%install
cd ../%{name}
install -d -m0755 %{buildroot}/%{bindir}/
install -d -m0755 %{buildroot}/%{libdir}/

install -p -m0755 src/unixcat %{buildroot}/%{bindir}/
install -p -m0644 src/livestatus.o %{buildroot}/%{libdir}/

cd %{buildroot}%{rgm_path}
ln -nsf %{name}-%{version} %{name}
cd -

%clean
rm -rf %{buildroot}

%files
%defattr(-, %{rgm_user_nagios}, %{rgm_group}, 0755)
%{linkdir}
%{datadir}

%changelog
* Wed Mar 20 2019 Samuel RONCIAUX <samuel.ronciaux@gmail.com> - 1.2.8p17-0.rgm
- Add macro paths

* Thu Feb 21 2019 Samuel RONCIAUX <samuel.ronciaux@gmail.com> - 1.2.8p17-0.rgm
- Initial RGM fork 

* Mon Feb 20 2017 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.8p17-0.eon
- upgrade to version 1.2.8p17

* Mon May 23 2016 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.8p1-0.eon
- upgrade to version 1.2.8p1

* Thu Dec 03 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.6p15-0.eon
- upgrade to version 1.2.6p15

* Tue Sep 29 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.6p12-0.eon
- upgrade to version 1.2.6p12

* Mon Aug 17 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.6p10-0.eon
- upgrade to version 1.2.6p10

* Mon May 18 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.6p2-0.eon
- upgrade to version 1.2.6p2

* Mon Mar 30 2015 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.6-0.eon
- upgrade to version 1.2.6

* Mon Nov 03 2014 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.4p5-0.eon
- upgrade to version 1.2.4p5

* Tue Jul 01 2014 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.4p4-0.eon
- upgrade to version 1.2.4p4

* Thu Mar 06 2014 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.4-0.eon
- packaged for EyesOfNetwork appliance 4.1

* Thu Apr 25 2013 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.2p2-0.eon
- packaged for EyesOfNetwork appliance 4.0

* Thu Jun 07 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.2.0p1-0.eon
- upgrade to version 1.2.0p1

* Tue Feb 28 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.12p7-0.eon
- upgrade to version 1.1.12p7

* Tue Jan 03 2012 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.12p6-0.eon
- upgrade to version 1.1.12p6

* Mon Dec 12 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.12p3-0.eon
- upgrade to version 1.1.12p3

* Thu Sep 08 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.10p3-0.eon
- upgrade to version 1.1.10p3

* Thu Mar 17 2011 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.10-0.eon
- upgrade to version 1.1.10

* Sun Nov 07 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.8-0.eon
- upgrade to version 1.1.8

* Thu Aug 05 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.6p1-0.eon
- upgrade to version 1.1.6p1

* Thu May 06 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.4-0.eon
- upgrade to version 1.1.4

* Sun Mar 28 2010 Jean-Philippe Levy <jeanphilippe.levy@gmail.com> - 1.1.3-0.eon
- packaged for EyesOfNetwork appliance 2.1
