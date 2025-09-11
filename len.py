from urllib.response import addbase

a=int(input("enter a number"))
b=int(input("enter a number"))
c=int(input("enter a choice"))
add=a+b
sub=a-b
mul=a*b
div=a/b
if c==1:
    print(add)
elif c==2:
    print(sub)
elif c==3:
    print(mul)
elif c==4:
    print(div)
else:
    print("error")