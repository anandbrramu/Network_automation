import paramiko
#from getpass import getpass
import time
import fileinput
import sys
import re
import paramiko

import time
import fileinput
import sys
import os
import fileinput
import sys
import re
import socket
import netmiko
import getpass
from getpass import getpass
import socket

device_list= input('enter the inventory list of devices in .txt format: ')
syslog=input('enter the syslog server IP based on the DC')
uname=input('Enter the username:')
passwd=getpass.getpass("Password: ")

ip = [i.strip() for i in open(device_list,'r')]

for ip1 in ip:
    #ip_list = []
    #ais = socket.getaddrinfo(ip1, 0, 0, 0, 0)
    #for result in ais:
    #    ip_list.append(result[-1][0])
    #ip_list = list(set(ip_list))
    #print(ip_list[0])
    cisco_881 = {
        'device_type':'cisco_ios',
        'ip':ip1,
        'username':uname,
        'password':passwd,
        'secret':passwd
        }
    SSHClass = netmiko.ssh_dispatcher(cisco_881['device_type'])
    try:
        net_connect = SSHClass(**cisco_881)
        print('device reachable')
        time.sleep(2)
        output = net_connect.send_command("show ip interface brief vrf all | in %s\n" %ip)
        time.sleep(4)
        print(output)
        interface=output.split(' ')
        print(interface[0])
        output = net_connect.send_command("show run interface %s\n" % interface[0])
        time.sleep(4)
        vrf = re.findall(r'vrf member(.*)', output)
        print(vrf[0])
        time.sleep(4)
        output = net_connect.send_config_set('logging server %s 6 facility local7 use-vrf %s\n' %(syslog,vrf[0]))
        #output = net_connect.send_config_set(command)
        time.sleep(2)
        print(output)
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print ('=== %s deviceBad credentials'%ip1)
    except netmiko.ssh_exception.NetMikoTimeoutException:
        print ('=== %s device unreachable'%ip1)
