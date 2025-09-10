def factorial(g):
    if g==0 or g==1:
       return 1
    else:
       return g * factorial(g-1)
print(factorial(8))
