#Q.4- Write a Python program to combine each line from first file with the corresponding line in second file.
with open('test.txt') as f1,open('test1.txt') as f2,open('test2.txt','w') as f3:
    for line1,line2 in zip(f1,f2):
        print(line1+line2)
        f3.write(line1)
        f3.write(line2)
    f3.close()
                
                
