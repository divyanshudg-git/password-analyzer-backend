from AdvancedPasswordAnalyzer import AdvancedPasswordAnalyzer
from password_classifier import PasswordClassifier
from password_generator import PasswordGenerator

# Define test cases for weak and strong passwords
test_cases = [
    # Weak / feature triggers
    {"password": "password123", "personal_info": ["divyansh", "2003", "india"], "desc": "Weak password, dictionary word, digits"},
    {"password": "divyansh2003", "personal_info": ["divyansh", "2003", "india"], "desc": "Password leaking personal info"},
    {"password": "123456", "personal_info": ["divyansh", "2003", "india"], "desc": "Common pattern password"},
    {"password": "qwertyuiop", "personal_info": ["divyansh", "2003", "india"], "desc": "Keyboard pattern password"},
    {"password": "pa$$w0rd", "personal_info": ["divyansh", "2003", "india"], "desc": "Password with common substitutions"},
    {"password": "aaaaaaBBB111", "personal_info": ["divyansh", "2003", "india"], "desc": "Password with character repetitions"},
    {"password": "letmein123", "personal_info": ["divyansh", "2003", "india"], "desc": "Known leak pattern password"},
    {"password": "HELLOworld123", "personal_info": ["divyansh", "2003", "india"], "desc": "Password with upper, lower, digits"},
    {"password": "abc!@#", "personal_info": ["divyansh", "2003", "india"], "desc": "Password with special characters only"},
    {"password": "dragonfly", "personal_info": ["divyansh", "2003", "india"], "desc": "Dictionary word password"},
    {"password": "India123", "personal_info": ["divyansh", "2003", "india"], "desc": "Named entity (country) password"},
    {"password": "X1#Z", "personal_info": ["divyansh", "2003", "india"], "desc": "Short random password (edge case)"},
    # Known reused password
    {"password": "markinho", "personal_info": ["divyansh", "2003", "india"], "desc": "Known reused password from breach list (rockyou.txt)"},
    # STRONG passwords
    {"password": "G7#u!n3Rk2!qPz", "personal_info": ["divyansh", "2003", "india"], "desc": "Strong random password with all character classes"},
    {"password": "F!8g$R3k#Lp2mN7w", "personal_info": ["divyansh", "2003", "india"], "desc": "Another strong password (16 chars, all char types)"},
    {"password": "Vx9$%m3Q!rB1*Nd6", "personal_info": ["divyansh", "2003", "india"], "desc": "Strong password with symbols scattered"},
    {"password": "3N*v9dF&xP!2Kz7#", "personal_info": ["divyansh", "2003", "india"], "desc": "Strong password, no dictionary words, no personal info"},
]

# Initialize the classifier
classifier = PasswordClassifier()

# Loop through test cases and evaluate each password
for case in test_cases:
    password = case["password"]
    personal_info = case["personal_info"]
    desc = case["desc"]

    # Initialize the analyzer with password and personal information
    analyzer = AdvancedPasswordAnalyzer(password, personal_info=personal_info)
    
    # Extract password features and check strength
    features = analyzer.check_password_strength()
    strength = classifier.predict_strength(password, personal_info)
    
    # Print results for each test case
    print(f"=========================")
    print(f"TEST CASE: {desc}")
    print(f"Password: {password}")
    print(f"Predicted Strength: {strength}")
    print(f"Entropy: {features['entropy']}")
    print(f"Has Upper: {features['has_upper']}")
    print(f"Has Lower: {features['has_lower']}")
    print(f"Has Digit: {features['has_digit']}")
    print(f"Has Special: {features['has_special']}")
    print(f"Personal Info Leak: {features['personal_info_leak']}")
    print(f"Password Reuse: {features['password_reuse']}")
    print(f"Common Patterns: {features['common_patterns']}")
    print(f"Named Entity Found: {features['named_entity']}")
    print(f"Character Classes Count: {features['char_classes_count']}")
    print(f"Keyboard Pattern: {features['keyboard_pattern']}")
    print(f"Leak Pattern: {features['leak_pattern']}")
    print(f"Repetition Detected: {features['repetition_detected']}")
    print(f"Common Substitution Detected: {features['common_substitution_detected']}")
    
    # Suggest a stronger password if the current password is weak
    if strength == "Weak":
        print(f"Suggested password: {PasswordGenerator().suggest_stronger_password(password)}")

    print(f"=========================\n")
