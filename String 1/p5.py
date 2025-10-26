#
def removePunctuations(text):
    punctuations = "!#$%&'()*+,-./:;<=>?@[]^_`{|}~"
    new_text =""
    for char in text:
        if char not in punctuations:
            new_text += char
    return new_text


removePunctuations = removePunctuations("Hello, world! How's it going?")
print("After Removing punctuations:",removePunctuations)