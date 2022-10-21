# You are using Python
def exch(n,i):
    l=[100,50,10,5,2,1]
    s = n // l[i]
    d = n % l[i]
    
    if d == 0:
        return s
    else:
        return s + exch(d,i+1)

n = int(input())
i = 0
print(exch(n,i))
