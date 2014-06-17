## Linux-disk-discovery ##

### Requirements ###

1. iostat

    yum install -y sysstat

### Installation ###

Agent

eg: /usr/local/zabbixagent

1. Update agentd.conf:

        vi /usr/local/zabbixagent/conf/zabbix_agentd.conf
        Include=/usr/local/zabbixagent/conf/zabbix_agentd
        :wq
2. Copy conf and script to zabbix agent directory.

        cp -r conf scripts /usr/local/zabbixagent/

3. Miscs.

        cd /usr/local/zabbixagent/
        mkdir tmp scripts
        chmod 775 tmp scripts
        touch tmp/iostats
        chmod 644 tmp/iostats
        touch scripts/discovery-linux.py
        chmod 754 scripts/discovery-linux.py
        chown zabbix:zabbix ./* -R

4. Restart

        nohup iostat -k -x -d 30 > /usr/local/zabbixagent/tmp/iostats &
        sudo service zabbix_agentd restart

5. Test: Change **10.0.0.1** and **sda** to your target.

        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.rps[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.wps[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.rkbps[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.wkbps[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.avgrq-sz[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.avgqu-sz[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.await[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.svctm[sda]'
        /usr/local/zabbixagent/bin/zabbix_get -s 10.0.0.1 -k 'io.util[sda]'

6. Add clean task in crontab.
        crontab -e
        59 8 * * * iostat -k -x -d 30 2 > /usr/local/zabbixagent/tmp/iostats &

7. Add configuration in frontend. Import the template.
8. Enjoy!