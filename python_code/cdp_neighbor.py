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

from shutil import copyfile

remote_conn_pre = paramiko.SSHClient()
remote_conn_pre.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ips = [i.strip() for i in open('list.txt','r')]
UN=open('unreachable.txt','w')
AE=open('Authentication_failed.txt','w')
RE=open('reachable.txt','w')
AL=open('alcatel.txt','w')
CDPD=open('cdp_detail.txt','w')
CDPI=open('cdp_inventory.txt','w')
CDPL = open('cdp_list.txt', 'w')
CISCO=open('cisco_sw.txt','w')
for ip in ips:
    try:
        remote_conn_pre.connect(ip, username='cisco', password='cisco', timeout=3)
        #stdin, stdout, stderr = remote_conn_pre.exec_command('sh ip ssh')
        #print ip + '===' + stdout.read()
        RE.write(ip)
        RE.write('\n')
        remote_conn_pre.close()
    except paramiko.AuthenticationException:
        AE.write(ip)
        UN.write('\n')
        print ip + '=== Bad credentials'
    except paramiko.SSHException:
        print ip + '=== Issues with ssh service'
    except socket.error:
        UN.write(ip)
        UN.write('\n')
        print ip + '=== Device unreachable'
UN.close()
RE.close()
AE.close()


ips = [i.strip() for i in open('reachable.txt','r')]
for ip in ips:
    remote_conn_pre.connect(ip, username='aramu', password='bonnie12')
    remote_conn = remote_conn_pre.invoke_shell()
    remote_conn.send("\n")
    output = remote_conn.recv(50000)
    time.sleep(1)
    print output
    remote_conn.send("\n")
    output = remote_conn.recv(50000)
    time.sleep(1)
    print output
    if '#' in output:
        CISCO.write(ip)
        CISCO.write('\n')
        print '\n----- Downloading CDP and Interface Information -----\n'
        remote_conn.send('terminal length 0\n')
        time.sleep(1)
        remote_conn.send("sh cdp neigh  detail\n")
        print '\t*** Getting CDP Neighbor  Detail ***'
        time.sleep(2)
        output = remote_conn.recv(50000)
        CDPD.write(output)

        print '\t*** Received CDP Neighbor Detail ***'

    else:
        AL.write(ip)
        AL.write('\n')

CDPD.close()
CISCO.close()
IP, model, hostname = '', '', ''

CDPR=open('cdp_detail.txt','r')
for data in CDPR:
    data_line = data.split('\n')
    for line in data_line:
        if 'Device ID: ' in line:
            (junk, hostname) = line.split('Device ID: ')
            hostname = hostname.strip()

        if 'IP address: ' in line:
            (junk, IP) = line.split('IP address: ')
            IP = IP.strip()

        if 'Platform: ' in line:
            (platform, capabilities) = line.split(',')
            (junk, model) = platform.split('Platform: ')
            model = model.strip()
            # if platform == "(.*)(cisco)(.*)":
        if 'Interface: ' in line:
            (loc_int, junk) = line.split(',')
            (junk, loc_int) = loc_int.split('Interface: ')
            loc_int = loc_int.strip()
            loc_int = re.sub('TenGigabitEthernet', 'Te', loc_int)
            loc_int = re.sub('GigabitEthernet', 'Gi', loc_int)
            loc_int = re.sub('FastEthernet', 'Fa', loc_int)
            if re.match("(.*)(cisco)(.*)", model):
                CDPI.write(IP)
                CDPI.write('                                     ')
                CDPI.write(hostname)
                CDPI.write('                                     ')
                CDPI.write(loc_int)
                CDPI.write('                                     ')
                CDPI.write(model)
                CDPI.write('\n')

CDPI.close()
with open('cdp_inventory.txt', 'r') as f:
    for line in f:
        CDPL.write(line.split(None, 1)[0])
        CDPL.write('\n')
CDPD.close()
CDPL.close()


uniqlines = set(open('cdp_list.txt','r').readlines())
u10 = open('cdp_list.txt', 'w').writelines(set(uniqlines))

ips = [i.strip() for i in open('cdp_list.txt','r')]
CDPD_1=open('cdp_detail_1.txt','w')
CDPI_1=open('cdp_inventory_1.txt','w')
CDPL_1 = open('cdp_list_1.txt', 'w')
for ip in ips:
    remote_conn_pre.connect(ip, username='aramu', password='bonnie12')
    remote_conn = remote_conn_pre.invoke_shell()
    remote_conn.send("\n")
    output = remote_conn.recv(50000)
    time.sleep(1)
    print output
    remote_conn.send("\n")
    output = remote_conn.recv(50000)
    time.sleep(1)
    print output
    print '\n----- Downloading CDP and Interface Information -----\n'
    remote_conn.send('terminal length 0\n')
    time.sleep(1)
    remote_conn.send("sh cdp neigh  detail\n")
    print '\t*** Getting CDP Neighbor  Detail ***'
    time.sleep(2)
    output = remote_conn.recv(50000)
    CDPD_1.write(output)

CDPD_1.close()

IP, model, hostname = '', '', ''

CDPR=open('cdp_detail_1.txt','r')
for data in CDPR:
    data_line = data.split('\n')
    for line in data_line:
        if 'Device ID: ' in line:
            (junk, hostname) = line.split('Device ID: ')
            hostname = hostname.strip()

        if 'IP address: ' in line:
            (junk, IP) = line.split('IP address: ')
            IP = IP.strip()

        if 'Platform: ' in line:
            (platform, capabilities) = line.split(',')
            (junk, model) = platform.split('Platform: ')
            model = model.strip()
            # if platform == "(.*)(cisco)(.*)":
        if 'Interface: ' in line:
            (loc_int, junk) = line.split(',')
            (junk, loc_int) = loc_int.split('Interface: ')
            loc_int = loc_int.strip()
            loc_int = re.sub('TenGigabitEthernet', 'Te', loc_int)
            loc_int = re.sub('GigabitEthernet', 'Gi', loc_int)
            loc_int = re.sub('FastEthernet', 'Fa', loc_int)
            if re.match("(.*)(cisco)(.*)", model):
                CDPI_1.write(IP)
                CDPI_1.write('                                     ')
                CDPI_1.write(hostname)
                CDPI_1.write('                                     ')
                CDPI_1.write(loc_int)
                CDPI_1.write('                                     ')
                CDPI_1.write(model)
                CDPI_1.write('\n')

CDPI_1.close()
E2=open('cdp_list_nest_1.txt','w')
with open('cdp_inventory_1.txt', 'r')as E1:
    for line in E1:
        if re.match("(.*)(SW)(.*)", line):
            E2.write(line)
E2.close()
with open('cdp_list_nest_1.txt', 'r') as f:
    for line in f:
        CDPL_1.write(line.split(None, 1)[0])
        CDPL_1.write('\n')
CDPL_1.close()

uniqlines = set(open('cdp_list_1.txt','r').readlines())
u10 = open('cdp_list_1.txt', 'w').writelines(set(uniqlines))


with open('cdp_list.txt', 'r') as file1:
    with open('cdp_list_1.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('output_1.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

with open('output_1.txt', 'r') as file1:
    with open('cdp_list_1.txt', 'r') as file2:
        same = set(file1).symmetric_difference(file2)

same.discard('\n')

with open('cdp_nest_3.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

ips = [i.strip() for i in open('cdp_nest_3.txt','r')]
CDPD_2=open('cdp_detail_2.txt','w')
CDPI_2=open('cdp_inventory_2.txt','w')
CDPL_2 = open('cdp_list_2.txt', 'w')
for ip in ips:
    remote_conn_pre.connect(ip, username='aramu', password='bonnie12')
    remote_conn = remote_conn_pre.invoke_shell()
    remote_conn.send("\n")
    output = remote_conn.recv(50000)
    time.sleep(1)
    print output
    remote_conn.send("\n")
    output = remote_conn.recv(50000)
    time.sleep(1)
    print output
    print '\n----- Downloading CDP and Interface Information -----\n'
    remote_conn.send('terminal length 0\n')
    time.sleep(1)
    remote_conn.send("sh cdp neigh  detail\n")
    print '\t*** Getting CDP Neighbor  Detail ***'
    time.sleep(2)
    output = remote_conn.recv(50000)
    CDPD_2.write(output)

CDPD_2.close()

IP, model, hostname = '', '', ''

CDPR=open('cdp_detail_2.txt','r')
for data in CDPR:
    data_line = data.split('\n')
    for line in data_line:
        if 'Device ID: ' in line:
            (junk, hostname) = line.split('Device ID: ')
            hostname = hostname.strip()

        if 'IP address: ' in line:
            (junk, IP) = line.split('IP address: ')
            IP = IP.strip()

        if 'Platform: ' in line:
            (platform, capabilities) = line.split(',')
            (junk, model) = platform.split('Platform: ')
            model = model.strip()
            # if platform == "(.*)(cisco)(.*)":
        if 'Interface: ' in line:
            (loc_int, junk) = line.split(',')
            (junk, loc_int) = loc_int.split('Interface: ')
            loc_int = loc_int.strip()
            loc_int = re.sub('TenGigabitEthernet', 'Te', loc_int)
            loc_int = re.sub('GigabitEthernet', 'Gi', loc_int)
            loc_int = re.sub('FastEthernet', 'Fa', loc_int)
            if re.match("(.*)(cisco)(.*)", model):
                CDPI_2.write(IP)
                CDPI_2.write('                                     ')
                CDPI_2.write(hostname)
                CDPI_2.write('                                     ')
                CDPI_2.write(loc_int)
                CDPI_2.write('                                     ')
                CDPI_2.write(model)
                CDPI_2.write('\n')

CDPI_2.close()
E2=open('cdp_list_nest_2.txt','w')
with open('cdp_inventory_2.txt', 'r')as E1:
    for line in E1:
        if re.match("(.*)(SW)(.*)", line):
            E2.write(line)
E2.close()
with open('cdp_list_nest_2.txt', 'r') as f:
    for line in f:
        CDPL_2.write(line.split(None, 1)[0])
        CDPL_2.write('\n')
CDPL_2.close()

uniqlines = set(open('cdp_list_2.txt','r').readlines())
u10 = open('cdp_list_2.txt', 'w').writelines(set(uniqlines))


with open('cdp_list_1.txt', 'r') as file1:
    with open('cdp_list_2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('output_2.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

with open('output_2.txt', 'r') as file1:
    with open('cdp_list_2.txt', 'r') as file2:
        same = set(file1).symmetric_difference(file2)

same.discard('\n')

with open('cdp_nest_4.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

filenames = ['cisco_sw.txt', 'cdp_list.txt', 'cdp_nest_3.txt', 'cdp_nest_4.txt']
with open('cdp_devices.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)

