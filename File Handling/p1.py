#Write a Python program to create a new text file and write user input to it.
def createFile(string):
    with open("myfile.txt",'w')as f1:
        f1.write(string)


string = "Hello this is my first file"
createFile(string)