user_name = input("Enter your user name: ")
password = input("Enter your password: ")
password_length = len(password)
hidden_password = '*' * password_length

print(f'Hello {user_name}, Your password {hidden_password} is {password_length} characters long.')