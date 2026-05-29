import getpass
import re

def audit_password(password):
    """
    Evaluates password strength and returns a list of policy violations.
    """
    failures = []
    
    # 1. Length Check
    if len(password) < 12:
        failures.append("Minimum 12 characters required.")
        
    # 2. Uppercase Check
    if not re.search(r'[A-Z]', password):
        failures.append("Missing an uppercase letter.")
        
    # 3. Lowercase Check
    if not re.search(r'[a-z]', password):
        failures.append("Missing a lowercase letter.")
        
    # 4. Digit Check
    if not re.search(r'\d', password):
        failures.append("Missing a numerical digit.")
        
    # 5. Special Character Check (Covers more symbols)
    if not re.search(r'[ !@#$%^&*(),.?":{}|<>]', password):
        failures.append("Missing a special character.")

    return failures

def main():
    print("--- Password Policy Audit Tool ---")
    
    # Using getpass so the password isn't visible on screen
    password = getpass.getpass("Enter password to test: ")
    
    violations = audit_password(password)
    
    if not violations:
        print("\n✅ Result: Strong Password! Meets all policy requirements.")
    else:
        print(f"\n❌ Result: Weak Password ({len(violations)} issues found):")
        for error in violations:
            print(f"  - {error}")

if __name__ == "__main__":
    main()
