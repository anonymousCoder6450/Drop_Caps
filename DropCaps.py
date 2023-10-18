#1. Initialize a variable `index` to 0.
#2. Read the input string `input_string`.
#3. While `index` is less than the length of `input_string`:
#     a. If `input_string[index]` is a space, increment `index`.
#     b. Otherwise, break the loop.
#4. If `index` is less than the length of `input_string`, the first non-space character is at `input_string[index]`.
#5. Display or return the first non-space character.


#1. Split the input string into words.
#2. For each word in the list of words:
#  a. If the length of the word is greater than 2, capitalize the first letter and make the rest lowercase.
#  b. Otherwise, keep the word as it is.
#3. Join the modified words back together using spaces.
#4. Return the modified string.


def drop_cap(word):
    words = word.split(' ')  # Split by space character
    modified_words = []

    for word in words:
        if len(word) > 2:
            modified_word = word[0].upper() + word[1:].lower()
        else:
            modified_word = word
        modified_words.append(modified_word)

    modified_string = ' '.join(modified_words)  # Join with space character
    return modified_string

x = drop_cap("HeLLo World")
print(x)
