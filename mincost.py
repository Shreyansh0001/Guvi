a,b=input().split()
n1=len(a)
n2=len(b)
if n2>n1:
    i=0
    while i<n1 and a[i]==b[i]:
        i+=1
    print(n2-i)
elif n2==n1:
    i=0
    while i<n2 and a[i]==b[i]:
        i+=1
    print(n2-i)
else:
    i=0
    while i<n2 and a[i]==b[i]:
        i+=1
    d=a[i:]
    z=b[i:]
    l=list(d)
    k=0
    for q in z:
        if q in l:
            k+=1
            l.remove(q)
    print(n1-i-k)
