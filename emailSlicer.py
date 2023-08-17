email = input("Enter your email:")

index = email.index('@')

username = email[:index]
domain = email[index:]

print(f"Your name is {username} and domain is {domain}")
