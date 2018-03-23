def say_helloM(name):
    print('hello Mr.%s')%name
def say_helloF(name):
    print ('hello Mrs. %s')%name


name=input('enter the name here')
Sex=input('enter the gender here')
if Sex=='M':
    say_helloM(name)
else:
    say_helloF(name)
