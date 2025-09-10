#program to search and count all occurrences of a character in a given string

def occur(str,ch):
    chcount=0
    pos=[]
    for i in range(len(str)):
        if str[i]==ch:
            chcount+=1
            pos.append(i)
            print(f"{str[i]} : at {pos} : {chcount}")
str=input("Enter string")
ch=input("Enter character")
occur(str,ch)