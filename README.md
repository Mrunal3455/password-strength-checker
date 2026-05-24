# 🔐 Password Strength Checker

A Python-based command-line application that evaluates the strength of a password and provides a score out of 100 with improvement tips.

---

## 📌 Features

- Checks password against 5 security criteria
- Gives a strength score out of 100
- Classifies password as **Strong**, **Moderate**, or **Weak**
- Provides specific tips to improve weak passwords
- Handles edge cases like empty input
- Continuous input loop — check multiple passwords in one run

---

## Tech Stack

- **Language:** Python 3
- **Modules:** `re` (Regular Expressions) — built-in, no installation needed

---

##  How to Run

1. Make sure Python 3 is installed on your system
2. Clone this repository:
   ```
   git clone https://github.com/Mrunal3455/password-strength-checker.git
   ```
3. Navigate to the project folder:
   ```
   cd password-strength-checker
   ```
4. Run the program:
   ```
   python password_checker.py
   ```

---

## 📊 Scoring Criteria

| Criteria                  | Points |
|---------------------------|--------|
| Length (8+ chars)         | 10     |
| Length (12+ chars)        | 20     |
| Length (16+ chars)        | 30     |
| Uppercase letters (A-Z)   | 20     |
| Lowercase letters (a-z)   | 20     |
| Numbers (0-9)             | 15     |
| Special characters (!@#$) | 15     |
| **Total**                 | **100**|

---

## 💡 Strength Labels

| Score     | Label    |
|-----------|----------|
| 80 – 100  | Strong 💪 |
| 50 – 79   | Moderate ⚠️ |
| 0 – 49    | Weak ❌  |

---

## 📸 Sample Output

```
🔐 Welcome to Password Strength Checker
   Type 'quit' to exit

Enter your password: hello

========================================
  Password Strength Checker
========================================
  Score     : 20/100
  Strength  : 🔴 Weak ❌
========================================

📋 Tips to improve your password:
   • Use at least 8 characters
   • Add at least one uppercase letter (A-Z)
   • Add at least one number (0-9)
   • Add a special character (!@#$%^&*)
```

---

**Mrunal Pansare**  
📧 mrunalpansare48645@gmail.com  
🔗 [LinkedIn](https://www.linkedin.com/in/mrunal-p-45280b259/)  
🐙 [GitHub](https://github.com/Mrunal3455)
