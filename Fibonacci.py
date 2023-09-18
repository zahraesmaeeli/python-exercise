def fib(n):
    if n==0:
        return 0
    if n==1:
        return 1
    return fib(n-1)+fib(n-2)

fibonnaci_list = list()
for i in range(0,8):
    fibonnaci_list.append(i)
    # print(fib(i))
print(list(reversed(fibonnaci_list)))