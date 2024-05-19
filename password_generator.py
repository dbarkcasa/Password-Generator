import random
import string

def generate_password(length=12):
    """Generate a random password."""
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    punctuation = string.punctuation

    # Combine all character sets
    all_chars = letters + digits + punctuation

    # Ensure the password has at least one character from each set
    password = [
        random.choice(letters),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Fill the rest of the password length with random choices
    password += random.choices(all_chars, k=length - 3)

    # Shuffle the resulting list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string and return
    return ''.join(password)

if __name__ == "__main__":
    # Set the desired password length
    password_length = 12
    # Generate the password
    password = generate_password(password_length)
    # Print the generated password
    print(f"Generated password: {password}")
