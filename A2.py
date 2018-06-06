#Q.2- Write a Python program to count the frequency of words in a file.
f=open("test.txt")
data=f.read()
words=data.split()
print("Total words= ",len(words))
f.close()
