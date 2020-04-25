i=int(input('Enter first:'))
j=int(input('Enter Second:'))

max=0
for k in range(i,j+1):
    s=[k]
    while k!=1:
        if k%2==0:
            k=k/2
            s.append(k)
        else:
            k=3*k+1
            s.append(k)
    if len(s)>max:
        max=len(s)
print(max)
