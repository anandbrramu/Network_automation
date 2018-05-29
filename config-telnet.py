import getpass
import sys
import telnetlib
import time



console_ip = sys.argv[1]
telnet_port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
hostname = sys.argv[5]
mgmt_ip = sys.argv[6]
mgmt_gw = sys.argv[7]

try:
    telnet = telnetlib.Telnet(console_ip,telnet_port)
    time.sleep(2)
    telnet.write("\n")
    telnet.read_until("ogin: ",3)
    telnet.write(username + "\n")
    if password:
       telnet.read_until("assword:",3)
       telnet.write(password + "\n")
    telnet.write("show ip int br\n")
    telnet.write("configure terminal\n")
    telnet.write('hostname ' + hostname)
    telnet.write("interface mgmt0\n")
    telnet.write('ip address ' + mgmt_ip + "/24")
    telnet.write("vrf member mgmt\n")
    telnet.write('ip route 0.0.0.0/0 ' + mgmt_gw)
    telnet.write("end\n")
    telnet.write("exit\n")
    print telnet.read_all()
except:
    print('unreachable')