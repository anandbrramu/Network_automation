import paramiko
from getpass import getpass
import time
import fileinput
import sys
import re
import paramiko
from getpass import getpass
import time
import fileinput
import sys
import os
import fileinput
import sys
import re
import socket
import netmiko

ip='192.168.134.25'
cisco_881 = {
    'device_type':'cisco_ios',
    'ip':ip,
    'username':'cisco',
    'password':'cisco123',
    'secret':'cisco123'
    }
SSHClass = netmiko.ssh_dispatcher(cisco_881['device_type'])
try:
    net_connect = SSHClass(**cisco_881)
    print('device reachable')
    time.sleep(1)
    output = net_connect.send_command("show ip interface brief vrf all | in %s\n" %ip)
    time.sleep(1)
    print(output)
    interface=output.split(' ')
    #print(interface[0])
    output = net_connect.send_command("show run interface %s\n" % interface[0])
    time.sleep(2)
    vrf = re.findall(r'vrf member(.*)', output)
    print(vrf[0])
    output = net_connect.send_command("show run interface %s\n" % interface[0])
    time.sleep(2)
    output = net_connect.send_config_set("logging server 1.1.1.1 5 use-vrf %s\n" % vrf[0])
    print(output)
except netmiko.ssh_exception.NetMikoAuthenticationException:
    print ('=== Bad credentials')
except netmiko.ssh_exception.NetMikoTimeoutException:
    print ('=== device unreachable')
