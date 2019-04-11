a=input()
a=int(a)
l=[]

for i in range(0,a):
    ap=input()
    l.append(ap)
common_prefix=[]

for i in zip(*l):
    if i.count(i[0])==len(i):
        common_prefix.append(i[0])
    else:
        break
d=''.join(common_prefix)
print(d)
