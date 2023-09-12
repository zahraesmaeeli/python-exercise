def f(n,m):
    count=0
    while n>0:
        if (n % 10)==m:
            count+=1
        n//=10
    return count

print(f(256878575,8))

