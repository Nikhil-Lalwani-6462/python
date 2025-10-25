#check if a string is a palindrome
def stringPalindrome(string):
    new_string = string.lower()
    reverse = new_string[::-1]
    isPalindrome = False
    if reverse == new_string:
        isPalindrome = True
    return isPalindrome

isPalindrome = stringPalindrome("Madam")
if isPalindrome is True:
    print("String is Palindrome")
else:
    print("String is not palindrome")
