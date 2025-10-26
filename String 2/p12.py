#.Find the longest word in a sentence
def longestWord(text):
    words = text.split()
    max = 0
    max1 = 0
    count = 0
    longest_word = ""
    diction = {}
    for word in words:
        count = 1
        for char in word:
            count += 1
        if count > max:
            max = count
            longest_word = word
    return longest_word
            
            




longestWord = longestWord("Python makes coding fun and productive")
print("Longest word in the text:",longestWord)