a={1,2,3,4,4,5,6,7,7}
print(a)

b=['x','v','b','n','m']
c=set(b)
print(c)

#union
a={1,2,3,4,5}
b={6,7,9}
s3=a|b
print(s3)

#intersection
a={1,6,8,9,4,3}
b={1,2,3,4,5,9}
c=a&b
print(c)

#difference
a={1,4,5,6,7,8}
b={1,3,5,8,2,0}
c=b-a
print(c)

#symmetric difference
a={1,2,3,4,5,6,
   'a'}
b={'a','b','c'}
c=a^b
print(c)

