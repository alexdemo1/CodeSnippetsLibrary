def is_palindrome(word):
    cleaned_word = "".join(word.lower().split())
    return cleaned_word == cleaned_word[::-1]

# Usage example
word = input("Enter a word: ")
if is_palindrome(word):
    print("It's a palindrome!")
else:
    print("It's not a palindrome.")
