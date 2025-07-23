import random
import string

class PasswordGenerator:
    def generate_password(self, length=14):
        characters = string.ascii_letters + string.digits + "!@#$%^&*()"
        return ''.join(random.choice(characters) for _ in range(length))

    def suggest_stronger_password(self, current_password):
        # Check if the password is weak and generate a strong alternative
        if len(current_password) < 14 or not any(c.isupper() for c in current_password) or \
           not any(c.islower() for c in current_password) or not any(c.isdigit() for c in current_password) or \
           not any(c in string.punctuation for c in current_password):
            # Generate a stronger password if current one is weak
            return self.generate_password(14)  # Generate a 14-character strong password
        
        # If the password is already strong enough, add a random character to increase strength
        strong_password = list(current_password)
        if not any(c.isupper() for c in strong_password):
            strong_password.append(random.choice(string.ascii_uppercase))
        if not any(c.islower() for c in strong_password):
            strong_password.append(random.choice(string.ascii_lowercase))
        if not any(c.isdigit() for c in strong_password):
            strong_password.append(random.choice(string.digits))
        if not any(c in string.punctuation for c in strong_password):
            strong_password.append(random.choice(string.punctuation))

        # Ensure length is at least 14 characters, even after appending
        while len(strong_password) < 14:
            strong_password.append(random.choice(string.ascii_letters + string.digits + string.punctuation))
        
        return ''.join(strong_password)
