#delete element form listr at a specified position

def del_el(l,pos):
    if (pos>=len(l)):
        print("No element to delete")
    else :
        del l[pos]
        print(f"After deleting {l}")


l=[1,2,3,4,5,6,7,8,9,10]
pos=15
del_el(l,pos)