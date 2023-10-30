import random

# Function to get valid user input within the specified range
def get_user_input():
    while True:
        user_input = input("Enter a number between 1 and 100: ")
        if user_input.isdigit():
            user_input = int(user_input)
            if 1 <= user_input <= 100:
                return user_input
            else:
                print("Please enter a number between 1 and 100.")
        else:
            print("Please enter a valid number.")

# Generate a random number between 1 and 100
random_number = random.randint(1, 100)

# Get valid user input
user_input = get_user_input()

# Check if the user input matches the random number
if user_input == random_number:
    print("Yes! The input matches the random number.")
else:
    print("No, the input doesn't match the random number.")
