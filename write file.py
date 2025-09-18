b=open('gokul.txt','r')
a=open('gokul2.txt','w')
c=b.readline()
while(c!=''):
    a.write(c)
    c=b.readline()
b.close()
a.close()

