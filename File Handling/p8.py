def replaceWord():
    # Open the file in read/write mode
    with open("myfile.txt", 'r+') as f1:
        # Read the file content
        content = f1.read()

        # Take words from user
        old_word = input("Enter the word to replace: ")
        new_word = input("Enter the new word: ")

        # Replace all occurrences
        updated_content = content.replace(old_word, new_word)

        # Move pointer to start of file and overwrite
        f1.seek(0)
        f1.write(updated_content)
        f1.truncate()   # remove any leftover old data

    print("All occurrences of '{}' have been replaced with '{}'.".format(old_word, new_word))

replaceWord()
