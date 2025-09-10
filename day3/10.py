''' A school stores student records as tuples in the format (rollno,name,marks)
Write a python program to :
1.store data of students in a list of tuples
2.print name of the student who scored tghe hightes marks
3.print all students who scored more than 75 marks'''

def student_data():
    l=[]
    print("1.add new student\t2.print topper\t3.print pass\t")
    while True:
        ch=int(input("Enter choice : "))
        if ch==1:
            rollno=input("Enter rollno")
            name=input("Enter name")
            marks=int(input("Enter marks"))
            t=(rollno,name,marks)
            l.append(t)
        elif ch==2:
            highest=l[0]
            for tupl in l:
                if tupl[2]>highest[2]:
                    highest=tupl
            print(highest)
        elif ch==3:
            for tupl in l:
                if tupl[2]>75:
                    print(tupl)
        else:
            exit(0)
student_data()    