#Q.5- Write a Python program to write 10 random numbers into a file. Read the file and then sort the numbers and then store it to another file.
from random import *
l=[]
f1=open("t1.txt","w")
for i in range(10):
    num=str(randint(1,10))
    for j in num:
        f1.write(j)
f1=open('t1.txt')
no=f1.read()
l=list(no)
l.sort()
f2=open("t2.txt","w")
f2.writelines(l)
f1.close()
f2.close()

