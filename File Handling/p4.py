#Write a program to count the number of words in a file.
def countWords():
    count = 0
    with open("myfile.txt",'r') as f1:
        f1 = f1.read()
        for words in f1.split():
            count += 1
    return count

count = countWords()
print("Count of words in the file:",count)
