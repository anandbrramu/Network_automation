import re
string =input("enter the string")
match=re.findall(r'the',string)
c=len(match)
print match,c




