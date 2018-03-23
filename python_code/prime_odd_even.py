x,y,z=0,0,0

for num in range (10,100):
    for i in range(2,num):
        if num%2==0:
            j=num/2
            x=x+1
            print ('this is an even number %d'%(num))
            break
        elif num%i==0:
            j=num/i
            y=y+1
            print('this is a odd number %d and multiples of %d * %d'%(num,i,j))
            break
    else:
            z=z+1
            print('this is a prime number %d'%(num))

print (x,y,z)

import sys
print (sys.version)