
n =5 
for x in list(range(n)) + list((reversed(range(n-1)))):
    a = n-x-1
    b = x*2+1
    print('{: <{w1}}{:*<{w2}}'.format('', '', w1 = a, w2 = b))
