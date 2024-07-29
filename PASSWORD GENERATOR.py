import random
import string

def generate_password(length, has_uppercase, has_numbers, has_special_chars):
    
    characters = string.ascii_lowercase
    if has_uppercase:
        characters += string.ascii_uppercase
    if has_numbers:
        characters += string.digits
    if has_special_chars:
        characters += string.punctuation

    password = []
    for _ in range(length):
        password.append(random.choice(characters))

    # Ensure the password has at least one character from each required category
    if has_uppercase and not any(c.isupper() for c in password):
        password[random.randint(0, length - 1)] = random.choice(string.ascii_uppercase)
    if has_numbers and not any(c.isdigit() for c in password):
        password[random.randint(0, length - 1)] = random.choice(string.digits)
    if has_special_chars and not any(c in string.punctuation for c in password):
        password[random.randint(0, length - 1)] = random.choice(string.punctuation)

    random.shuffle(password)
    return ''.join(password)

def main():
    print("Welcome to the Password Generator!")
    length = int(input("Enter the desired length of the password: "))

    has_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    has_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    has_special_chars = input("Include special characters? (y/n): ").lower() == 'y'

    password = generate_password(length, has_uppercase, has_numbers, has_special_chars)
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
