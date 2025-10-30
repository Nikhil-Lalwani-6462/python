#Write a program to count the number of lines in a file
def countLines():
    count = 0
    with open("myfile.txt",'r') as f1:
        for line in f1:
            print(line)
            count += 1
    return count

count = countLines()
print("Number of lines in the file:",count)