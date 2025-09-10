#write program to count total no of words in a string 

def totwords(str):
    wcount=1
    for i in str:
        if i==" ":
            wcount+=1
    print(wcount)

str=input("Enter string : ")
totwords(str)

stri=input("Enter string to find words using split()")
words=stri.split()
print(len(words))