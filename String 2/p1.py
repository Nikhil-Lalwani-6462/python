#Reverse a string without using slicing or reversed()
def reverseString(string):
    end = len(string)-1
    start = 0
    ReverseString = ""
    while(end >= start):
        ReverseString += string[end]
        end -= 1
    return ReverseString

reverseString = reverseString("Hello")
print("After reverse a string without using reversed and slicing:",reverseString)