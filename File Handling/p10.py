#Write a program to read a file and print the longest word
def printLongest():
    max = 0 
    longest = ""
    count = 0
    
    with open("myfile.txt","r") as f1:
        conten = f1.read()
        for word in conten.split():
            count = 0
            for char in word:
                count += 1
            if count > max:
                max = count
                longest = word
    return longest
Longest = printLongest()
print("Longest word in the file:",Longest)


