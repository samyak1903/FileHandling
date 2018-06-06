#Q.3- Write a Python program to copy the contents of a file to another file
with open("test.txt") as f:
    with open("test1.txt", "w") as f1:
        for line in f:
            f1.write(line)
        print("Conents Copied")
        f1.close()
    f.close()
