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

sccm = input("enter the file name - Mention .csv extension with filename (format MM_DD_YY_HH_MM): ")

list = [i.strip() for i in open('list.txt','r')]
uname=input('Enter the username:')
passwd = getpass.getpass("Password: ")
for ip1 in store:
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
        time.sleep(1)
        line=open('config.txt','r')
        output=net_connect.send_config_from_file(config_file='config.txt')
        print(output)
        time.sleep(4)
        output = net_connect.send_command("end\n")
        time.sleep(1)
        # print(output)
        output = net_connect.send_command("wr mem\n")
        time.sleep(5)
        print(output)
        net_connect.disconnect()
        with open(sccm, 'a', newline='') as csvfile:
                spamwriter = csv.writer(csvfile, delimiter='~',
                                        quotechar='~', quoting=csv.QUOTE_MINIMAL)
                spamwriter.writerow([ip1, "completed"])

    except netmiko.ssh_exception.NetMikoAuthenticationException:
        print(ip1, 'Authentication Failed')
        with open(sccm, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='~',
                                    quotechar='~', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([ip1, "Authentication Failed"])

    except netmiko.ssh_exception.NetMikoTimeoutException:
        print(ip1,'Store  unreachable')
        with open(sccm, 'a', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter='~',
                                    quotechar='~', quoting=csv.QUOTE_MINIMAL)
            spamwriter.writerow([ip1, "device Unreachable"])
