#Add elements to set runtime
def addSet():
    a=set()
    n=int(input("Enter no of elements to add"))
    for i in range(n):
        a.add(input(f"Enter data element : {i} :"))
    print(a)
addSet()