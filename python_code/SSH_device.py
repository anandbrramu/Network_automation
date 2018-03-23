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
for ip in ips:
    try:
        remote_conn_pre.connect(ip, username='cisco', password='cisco', timeout=3)

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
