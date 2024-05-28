capacity=4
processlist=[0,7,1,0,2,9,3,0,4,0,2,3,0,3,2,0]
s=[]
pagefaults=0
for i in processlist:
    if i not in s:
        if (len(s)==capacity):
            s.remove(s[0])
            s.append(i)
        else:
            s.append(i)
        pagefaults=pagefaults+1
    else:
        s.remove(i)
        s.append(i)
print("{}".format(pagefaults))