def solution(n):
    z=list(range(1,n+1))
    start=0
    end=start+1
    cnt=0
    while start<end:
        if sum(z[start:end])<n:
            end=end+1
        elif sum(z[start:end])>n:
            start=start+1
        else:
            cnt+=1
            start+=1
    return cnt
solution(15)


def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
