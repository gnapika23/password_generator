import random
import string

def generate_password(length):
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation
    
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(special)
    ]
    
    all_chars = lower + upper + digits + special
    password += random.choices(all_chars, k=length-4)
    random.shuffle(password)
    return ''.join(password)

def generate_passwords(length, count):
    return [generate_password(length) for _ in range(count)]

def main():
    print("Welcome to the Password Generator!")
    try:
        length = int(input("Enter the length of the passwords: "))
        count = int(input("Enter the number of passwords to generate: "))
        
        if length < 4:
            print("Password length should be at least 4 to include all character types.")
            return

        passwords = generate_passwords(length, count)
        print("\nGenerated Passwords:")
        for password in passwords:
            print(password)
    except ValueError:
        print("Please enter valid integers for length and count.")

if __name__ == "__main__":
    main()
