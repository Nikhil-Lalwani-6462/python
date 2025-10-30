#.Write a program to read a file and print only lines that start with a vowel.
def vowelLine():
    f1 = open("myfile1.txt",'r')
    vowels = "aeiouAEIOU"
    for content in f1:
        for i in range(1):
            if content[i] in vowels:
                print(content)
            

vowelLine()
    