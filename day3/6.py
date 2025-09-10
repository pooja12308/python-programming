#frequency of element in list
def freq(l):
    fl={}
    for element in l:
        if element not in fl:
            fl[element]=1
        else:
            fl[element]+=1
    print(fl)
l=[1,1,2,3,4,4,5,5,5,6,7,6,6]
freq(l)