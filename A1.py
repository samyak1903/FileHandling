#Q.1- Write a Python program to read last n lines of a file
f=open("test.txt")
lines=f.readlines()
n=int(input("Enter the number of lines"))
l=lines[-n:]
print("Last {} lines of code are".format(n))
for i in l:
    print(i,end='')
f.close()
