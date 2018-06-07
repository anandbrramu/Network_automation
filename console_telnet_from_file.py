import getpass
import sys
import telnetlib


console_ip = sys.argv[1]
telnet_port = sys.argv[2]
username = sys.argv[3]
password = sys.argv[4]
hostname = sys.argv[5]
mgmt_ip = sys.argv[6]
mgmt_gw = sys.argv[7]

file=open("config.txt",'r') # open the config template .txt file
tn = telnetlib.Telnet(console_ip,telnet_port) # connecting socket
tn.write( "\n")
try:
    response = tn.read_until("login:", timeout=5) #or whatever timeout you choose.
except:
    print("nothing")

if 'login' in response:
    tn.write(username + "\n")
    tn.read_until("Password: ")
    tn.write(password + "\n")
    print("task completed")
    for line in file:
        print(line)
        tn.write(line + "\n") # write the commands line by line to the device
    tn.write("end\n")
    tn.write("exit\n")
    print("task completed with login prompt")
elif '#' in response:
    for line in file:
        print(line)
        tn.write(line + "\n")
    tn.write("end\n")
    tn.write("exit\n")
    print("task completed without login prompt")
else:
    print("unable to conect to console")
file.close()
