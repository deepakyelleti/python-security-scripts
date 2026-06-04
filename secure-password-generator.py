import secrets
import string


def generate_password(length=16):
    """
    Generate a secure password containing:
    - Uppercase letters
    - Lowercase letters
    - Numbers
    - Special characters
    """

    if length < 12:
        raise ValueError(
            "Password length should be at least 12 characters."
        )

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!@#$%^&*()-_=+[]{}<>?"

    # Ensure at least one character from each category
    password = [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(special)
    ]

    # Create combined character pool
    all_characters = lowercase + uppercase + digits + special

    # Fill remaining characters
    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle securely
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


def password_strength(password):
    """
    Evaluate password complexity.
    """

    checks = {
        "Uppercase": any(c.isupper() for c in password),
        "Lowercase": any(c.islower() for c in password),
        "Numbers": any(c.isdigit() for c in password),
        "Special Characters": any(
            c in "!@#$%^&*()-_=+[]{}<>?"
            for c in password
        ),
        "Length >= 12": len(password) >= 12
    }

    return checks


def main():

    print("=" * 50)
    print("Secure Password Generator")
    print("=" * 50)

    try:
        length = int(
            input(
                "\nEnter desired password length "
                "(minimum 12): "
            )
        )

        password = generate_password(length)

        print("\nGenerated Password:")
        print(password)

        print("\nPassword Strength Check:")
        print("-" * 30)

        checks = password_strength(password)

        for check, result in checks.items():
            status = "PASS" if result else "FAIL"
            print(f"{check:<20} {status}")

    except ValueError as e:
        print(f"\n[ERROR] {e}")

    except Exception as e:
        print(f"\nUnexpected Error: {e}")


if __name__ == "__main__":
    main()
