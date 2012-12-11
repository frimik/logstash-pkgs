# logstash-pkgs

logstash-pkgs contains simple files to build a RPM from a spec file.

## Creating RPM
Just copy the following files to the SOURCES directory:

    logstash-agent.conf
    logstash-agent.defaults
    logstash-agent.grok
    logstash-agent.init
    logstash.logrotate

Do not forget to download logstash to the SOURCES directory:

    http://logstash.objects.dreamhost.com/release/logstash-1.1.5-monolithic.jar

Then copy the following file to the SPECS directory:

    logstash.spec

Now you should be ready to build logstash with rpmbuild.

## HowTo

### Start and stop the logstash agent

    /etc/init.d/logstash-agent [ start | stop | restart ]

### Change init parameter

    /etc/sysconfig/logstash-agent

### Agent Configuration

    /etc/logstash/agent.conf

### Configuraton directories for patterns and plugins

    /etc/logstash/patterns
    /etc/logstash/plugins

### Logrotate

    /etc/logrotate.d/logstash

### Logfile

    /var/log/logstash/agent.conf

Have fun!
