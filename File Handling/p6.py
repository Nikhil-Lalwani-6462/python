#Write a program to copy the contents of one file into another.
def copyContent():
    f1 = open("myfile.txt",'r')
    f2 = open("myfile1.txt",'w')
    f1 = f1.read()
    f2.write(f1)
copyContent()