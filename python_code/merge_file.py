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
from shutil import copyfile

filenames = ['test1.txt', 'test2.txt', 'test3.txt','test4.txt']
with open('test5.txt', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)
