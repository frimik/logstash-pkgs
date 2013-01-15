Summary: logstash is a tool for managing events and logs.
Name: logstash
Version: 1.1.9
Release: 1%{?dist}
License: Apache 2.0
Group: System Environment/Daemons
Distribution: RHEL and CentOS
URL: http://logstash.net

Source0: http://logstash.objects.dreamhost.com/release/%{name}-%{version}-monolithic.jar
Source1: logstash-agent.init
Source2: logstash-agent.conf
Source3: logstash-agent.defaults
Source4: logstash.logrotate
Source5: logstash-agent.grok

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-%(%{__id_u} -n)
BuildArch: noarch

Requires: jre-openjdk

%define initdir %{_sysconfdir}/rc.d/init.d
%define confdir %{_sysconfdir}/logstash
%define logrdir %{_sysconfdir}/logrotate.d
%define logdir %{_var}/log/logstash
%define libdir %{_var}/lib/logstash
%define defaults %{_sysconfdir}/sysconfig
%define jardir /usr/share/logstash

%description
logstash is a tool for managing events and logs. You can use it to collect logs, parse them, and store them for later use (like, for searching). Speaking of searching, logstash comes with a web interface for searching and drilling into all of your logs.

%prep
true

%build
true

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{libdir}
mkdir -p %{buildroot}%{logdir}
install -D -m 644 %{SOURCE0} %{buildroot}%{jardir}/logstash-monolithic.jar
install -D -m 755 %{SOURCE1} %{buildroot}%{initdir}/logstash-agent
install -D -m 644 %{SOURCE2} %{buildroot}%{confdir}/agent.conf
install -D -m 644 %{SOURCE3} %{buildroot}%{defaults}/logstash-agent
install -D -m 644 %{SOURCE4} %{buildroot}%{logrdir}/logstash
install -D -m 644 %{SOURCE5} %{buildroot}%{confdir}/patterns/grok.conf

%pre
getent group logstash >/dev/null || /usr/sbin/groupadd logstash
getent passwd logstash >/dev/null || /usr/sbin/useradd \
    logstash -g logstash -s /sbin/nologin -d /usr/share/logstash -r

%post
true

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)

%{initdir}/logstash-agent
%{jardir}/logstash-monolithic.jar

%dir %attr(0750, logstash, logstash) %{confdir}
%dir %attr(0750, logstash, logstash) %{libdir}
%dir %attr(0750, logstash, logstash) %{logdir}
%config(noreplace) %attr(0640, logstash, logstash) %{confdir}/agent.conf
%config(noreplace) %attr(0640, logstash, logstash) %{confdir}/patterns/grok.conf
%config(noreplace) %attr(0640, root, root) %{logrdir}/logstash
%config(noreplace) %attr(0640, root, root) %{defaults}/logstash-agent

%changelog
* Tue Jan 15 2013 Jonny Schulz <js@bloonix.de> - 1.1.9-1
- Logstash 1.1.9 is released.
* Mon Jan 14 2013 Jonny Schulz <js@bloonix.de> - 1.1.8-1
- Logstash 1.1.8 is released.
* Fri Jan 04 2013 Jonny Schulz <js@bloonix.de> - 1.1.7-1
- Logstash 1.1.7 is released.
* Thu Nov 29 2012 Jonny Schulz <js@bloonix.net> - 1.1.5-2
- Replaced JAVA_MEM with JAVA_MEM_MIN and JAVA_MEM_MAX.
* Thu Nov 13 2012 Jonny Schulz <js@bloonix.net> - 1.1.5-1
- Logstash 1.1.5 released at 2012-11-10. Big thanks to Jordan.
* Thu Oct 22 2012 Jonny Schulz <js@bloonix.net> - 1.1.1-2
- Fixed the path to the default logstash arguments.
* Thu Oct 18 2012 Jonny Schulz <js@bloonix.net> - 1.1.1-1
- Initial package.
