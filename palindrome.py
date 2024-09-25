# Function to check if a string or number is a palindrome
def is_palindrome(input_value):
    # Convert to string and remove spaces and make it case insensitive
    sanitized_input = str(input_value).replace(" ", "").lower()
    return sanitized_input == sanitized_input[::-1]

# Input from the user
user_input = input("Enter a string or number: ")

# Check if it's a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome.")
else:
    print(f"'{user_input}' is not a palindrome.")
