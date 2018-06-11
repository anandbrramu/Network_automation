import csv
import paramiko
from getpass import getpass
import time
import fileinput
import sys
import re
import paramiko
import getpass
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
import subprocess
import csv
import paramiko
from getpass import getpass
import time
import fileinput
import sys
import re
import paramiko
import getpass
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
import subprocess
from netmiko import ConnectHandler
#from serial import serialcli


ip = [i.strip() for i in open('list.txt','r')]
interface_status = "interface_description.csv"

uname=input('Enter the username:')
passwd=input('Enter the Password: ')
for ip1 in ip:
    cisco_881 = {
        'device_type': 'cisco_ios',
        'ip': ip1,
        'username': uname,
        'password': passwd,
        'secret': passwd
    }
    print(ip1)
    SSHClass = netmiko.ssh_dispatcher(cisco_881['device_type'])
    try:
        net_connect = SSHClass(**cisco_881)
        net_connect.enable()
        vpc_role='"vPC role"'
        vpc = net_connect.send_command("sh vpc role | in %s \n"%vpc_role)
        #print(vpc)
        (junk, role1) = vpc.split('vPC role')
        role = role1.strip()
        print(role)
        count = net_connect.send_command("show interface status | in connected | count")
        description = net_connect.send_command("show interface description")
        with open(interface_status, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='~',
                                    quotechar='~', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([ip1, role, count, description])
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print ('=== %s deviceBad credentials'%ip1)
        with open(interface_status, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='~',
                                    quotechar='~', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([ip1, "bad credentials"])

    except netmiko.ssh_exception.NetMikoTimeoutException:
        print(ip1,'  unreachable')
        with open(interface_status, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='~',
                                    quotechar='~', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([ip1, "Unreachable"])
