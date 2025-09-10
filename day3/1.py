def list_fn():
    n = int(input("Enter number of elements: "))
    l = []
    
    for i in range(n):
        element = input()
        l.append(element) 
    print(l)

list_fn()
