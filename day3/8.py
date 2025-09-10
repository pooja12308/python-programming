#program to count total duplicates
def dfreq(l):
    fl={}
    for element in l:
        if element not in fl:
            fl[element]=1
        else:
            fl[element]+=1
    print(fl)
    for val in fl:
        if (fl[val]!=1):
            print(val)
l=[1,1,2,3,4,4,5,5,5,6,7,6,6]
dfreq(l)