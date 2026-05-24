import re

def check_length(password):
    """Check if password meets minimum length requirement."""
    return len(password) >= 8

def has_uppercase(password):
    """Check if password contains at least one uppercase letter."""
    return bool(re.search(r'[A-Z]', password))

def has_lowercase(password):
    """Check if password contains at least one lowercase letter."""
    return bool(re.search(r'[a-z]', password))

def has_digit(password):
    """Check if password contains at least one number."""
    return bool(re.search(r'[0-9]', password))

def has_special_char(password):
    """Check if password contains at least one special character."""
    return bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

def calculate_score(password):
    """Calculate password strength score out of 100."""
    score = 0
    tips = []

    # Length check - up to 30 points
    if len(password) >= 16:
        score += 30
    elif len(password) >= 12:
        score += 20
    elif len(password) >= 8:
        score += 10
    else:
        tips.append("Use at least 8 characters")

    # Uppercase check - 20 points
    if has_uppercase(password):
        score += 20
    else:
        tips.append("Add at least one uppercase letter (A-Z)")

    # Lowercase check - 20 points
    if has_lowercase(password):
        score += 20
    else:
        tips.append("Add at least one lowercase letter (a-z)")

    # Digit check - 15 points
    if has_digit(password):
        score += 15
    else:
        tips.append("Add at least one number (0-9)")

    # Special character check - 15 points
    if has_special_char(password):
        score += 15
    else:
        tips.append("Add a special character (!@#$%^&*)")

    return score, tips

def get_strength_label(score):
    """Return strength label based on score."""
    if score >= 80:
        return "Strong 💪", "✅"
    elif score >= 50:
        return "Moderate ⚠️", "🟡"
    else:
        return "Weak ❌", "🔴"

def check_password(password):
    """Main function to check password strength."""
    
    # Edge case - empty password
    if not password:
        print("\n❌ Password cannot be empty.\n")
        return

    score, tips = calculate_score(password)
    strength_label, icon = get_strength_label(score)

    print("\n" + "="*40)
    print(f"  Password Strength Checker")
    print("="*40)
    print(f"  Score     : {score}/100")
    print(f"  Strength  : {icon} {strength_label}")
    print("="*40)

    if tips:
        print("\n📋 Tips to improve your password:")
        for tip in tips:
            print(f"   • {tip}")
    else:
        print("\n🎉 Your password is very strong!")

    print()

def main():
    """Entry point of the program."""
    print("\n🔐 Welcome to Password Strength Checker")
    print("   Type 'quit' to exit\n")

    while True:
        password = input("Enter your password: ")

        if password.lower() == 'quit':
            print("\n👋 Goodbye!\n")
            break

        check_password(password)

if __name__ == "__main__":
    main()
