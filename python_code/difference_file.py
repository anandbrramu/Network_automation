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

with open('test1.txt', 'r') as file1:
    with open('test2.txt', 'r') as file2:
        same = set(file1).intersection(file2)

same.discard('\n')

with open('output_1.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)

with open('output_1.txt', 'r') as file1:
    with open('test1.txt', 'r') as file2:
        same = set(file1).symmetric_difference(file2)

same.discard('\n')

with open('output_2.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
