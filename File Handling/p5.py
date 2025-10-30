#Write a program to append new content to an existing file.
def appendContent():
    with open("myfile.txt","a") as f1:
        f1.write("This line is added later")

appendContent()