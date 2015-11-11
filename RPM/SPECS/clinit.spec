Name:		   clinit
Version:	   1.0
Release:	   ssv1%{?dist}
Summary:	   control daemon processes in cluster environment
Group:      System Environment/Libraries
BuildArch:  noarch
License:	   BSD
URL:	  	   https://github.com/sergevs/clinit
Source0:	   %name-%version.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%version-buildroot

%description
The clinit is a lightweight console cluster manager tool to manage services across multiply hosts respecting dependencies.
It does not require any agents on cluster nodes but relays on sshd as the transport and 
can perform LSB compliant actions to start/stop or show the status of a service in the cluster. 
Also it's able to visualize the services dependencies tree in a convenient way to show the overall cluster picture.
The syntax of clinit configuration file is pretty simple and sysadmin freindly.

%prep
%setup -q

%build

%install
%__rm -rf %buildroot
%__mkdir_p %buildroot%_bindir
%__mkdir_p %buildroot/etc/%name
%__install %name %buildroot%_bindir
%__install services.xml %buildroot/etc/%name


%files
%defattr(-,root,root)
%_bindir/*
%dir /etc/%name
%config(noreplace) /etc/%name/services.xml
%doc AUTHORS sample

%changelog
* Mon Nov 09 2015 Serge <abrikus@gmail.com> 1.0-ssv1
- initial release
