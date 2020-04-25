a=dict()
with open('word counting.txt','r') as f:
    words=[w.strip(',.') fo w in f.read().split()] #line 5~8 한번에
'''
    flie=f.read()
    words=flie.split(' ')
    for word in words:
        word.strip('.,') #이렇게 가능
'''
        a[word]=a.get(word,0)+1
temp=[]
for k,v in a.items():
    temp.append((v,k))
temp.sort(reverse=True)
for key,value in temp[:10]:
    print(value,key)

#print(words)
