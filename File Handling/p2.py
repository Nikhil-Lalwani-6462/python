#Write a program to read and display the contents of a file.
def readFile():
    with open("myfile.txt","r")as f1:
        f1 = f1.read()
    return f1

string = readFile()
print("Content in the file:",string)
