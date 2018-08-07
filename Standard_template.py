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

device_status = input("enter the file name - Mention .csv extension with filename = ")
ip = [i.strip() for i in open('list.txt','r')]
uname=input('Enter the username:')
passwd=input('Enter the Password: ')
#uname='cisco'
#passwd='cisco@123'
for ip1 in ip:
    cisco_881 = {
        'device_type': 'cisco_ios',
        'ip': ip1,
        'username': uname,
        'password': passwd,
        'secret': passwd
    }
    SSHClass = netmiko.ssh_dispatcher(cisco_881['device_type'])
    try:
        net_connect = SSHClass(**cisco_881)
        net_connect.enable()
        output = net_connect.send_command("\n")
        print(output)
        output = net_connect.send_command('show version')
        #print(output)
        if "IOS" in output:
            output = net_connect.send_config_from_file(config_file='std_templates/ios_template.txt')
            print(output)
            time.sleep(1)
            net_connect.disconnect()
            with open(device_status, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "IOS", "completed"])
        elif "NX-OS" in output:
            output = net_connect.send_config_from_file(config_file='std_templates/nxos_template.txt')
            print(output)
            time.sleep(1)
            net_connect.disconnect()
            with open(device_status, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "NXOS", "completed"])
        elif "Arista" in output:
            output = net_connect.send_config_from_file(config_file='std_templates/arista_template.txt')
            print(output)
            time.sleep(1)
            net_connect.disconnect()
            with open(device_status, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "Arista", "completed"])
        else:
            print("device not recognized")
            with open(device_status, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "device not recognized"])
    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print ('=== %s deviceBad credentials'%ip1)
        with open(device_status, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "bad-credentials"])
    except netmiko.ssh_exception.NetMikoTimeoutException:
        print(ip1,'device unreachable')
        with open(device_status, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "time-out"])


