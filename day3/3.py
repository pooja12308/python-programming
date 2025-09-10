#displaying second largest number in list
def larg_fn():
    n=int(input("Enter no of elements"))
    l=[]
    for i in range(n):
        element=input()
        l.append(element)
    print(f"list : {l}")
    l.sort(reverse=True)
    print("second largest element in the list is ")
    print(l[1])

larg_fn()