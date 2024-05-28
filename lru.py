
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
