def is_palindrome(word):
    # Convert the word to lowercase and remove non-alphanumeric characters
    word = ''.join(char.lower() for char in word if char.isalnum())
    return word == word[::-1]

user_input = input("Enter a word or phrase: ")
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
