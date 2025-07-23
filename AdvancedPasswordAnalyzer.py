from password_analyzer import PasswordAnalyzer
import re

# detect common keyboard patterns
KEYBOARD_PATTERNS = ["qwerty", "asdf", "zxcvbn", "12345", "password", "letmein"]

# detect typical substitutions
SUBSTITUTIONS = {
    '@': 'a',
    '4': 'a',
    '0': 'o',
    '$': 's',
    '5': 's',
    '1': 'l',
    '3': 'e'
}

# from password_analyzer import password_analyzer  # Replace with the actual module name

class AdvancedPasswordAnalyzer(PasswordAnalyzer):
    def __init__(self, password, personal_info=None):
        super().__init__(password)
        self.personal_info = personal_info or []

    def check_keyboard_pattern(self):
        for pattern in KEYBOARD_PATTERNS:
            if pattern in self.password.lower():
                return True
        return False

    def check_leak_patterns(self):
        # simulate checking against leaked passwords
        leaked_samples = ["123456", "password", "123123", "qwerty123"]
        for leak in leaked_samples:
            if leak in self.password.lower():
                return True
        return False

    def check_personal_info(self):
        return any(info.lower() in self.password.lower() for info in self.personal_info)

    def detect_repetitions(self):
        return bool(re.search(r"(..+?)\1{1,}", self.password))  # repeated sequences

    def detect_common_substitutions(self):
        normalized = ''.join(SUBSTITUTIONS.get(c.lower(), c.lower()) for c in self.password)
        return normalized == "password"

    def extract_advanced_features(self):
        features = super().extract_advanced_features()
        features.update({
            "keyboard_pattern": self.check_keyboard_pattern(),
            "leak_pattern": self.check_leak_patterns(),
            "personal_info_match": self.check_personal_info(),
            "repetition_detected": self.detect_repetitions(),
            "common_substitution_detected": self.detect_common_substitutions()
        })
        return features
