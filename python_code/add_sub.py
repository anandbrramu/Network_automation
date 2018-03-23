def add(x,y):
    '''this is addition'''
    return x+y
def sub(x,y):
    ''' this is subtraction'''
    return x-y

a=input('enter the vlaue of a')
b=input('enter the vlaue of b')
c=input('enter the function to perform ')
if c=='sum':
    print add(a,b)
elif c=='sub':
    print sub(a,b)
else:
    print ('enter the appropriate vlaues')

