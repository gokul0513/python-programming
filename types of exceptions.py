#index error
a=[1,2,3,4]
try:
    print(a[5])
except IndexError:
    print("index does not exist")

#type error
a='abc'
b=22
try:
    c=a+b

    print(c)
except TypeError:
    print("type does not exist")

#name error
a='abc'
try:
    print(g)
except NameError:
    print("name does not exist")

#value error

try:
    a=int('bb')
    print(a)
except ValueError:
    print("value does not exist")

#filenotfound error
try:
    a=open('krishnan.txt','r')
    print(a.readline())
except FileNotFoundError:
    print("file doesnot exist")

