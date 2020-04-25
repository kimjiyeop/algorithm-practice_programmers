def solution(n):
    a=[1,2]
    x=a[-1]
    y=a[-2]
    for j in range(n-2):
        x,y=(x+y)%1000000007,x%1000000007
        a.append(x)
    return a[-1]
from math import factorial
print(factorial(5)/factorial(3))

print('hello')
