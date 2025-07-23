import math
import re
import string
import spacy
import hashlib
from spacy import load
from password_generator import PasswordGenerator
from typing import List

nlp = load("en_core_web_sm")

class PasswordAnalyzer:
    def __init__(self, password: str, personal_info: List[str] = None):
        self.password = password
        self.personal_info = personal_info or []

    def calculate_entropy(self):
        prob = [float(self.password.count(c)) / len(self.password) for c in set(self.password)]
        return -sum([p * math.log2(p) for p in prob])

    def check_dictionary(self, wordlist: List[str]):
        return any(word in self.password.lower() for word in wordlist)

    def check_semantics(self):
        doc = nlp(self.password)
        return [ent.label_ for ent in doc.ents]

    def check_password_reuse(self,password):
        try:
            with open('rockyou.txt', 'r', encoding='utf-8', errors='ignore') as file:
                breached_passwords = set(line.strip() for line in file)
            return password in breached_passwords
        except FileNotFoundError:
            print("Breached password list not found.")
            return False

    def check_common_patterns(self):
        # Checks for simple patterns like "12345", "qwerty", etc.
        common_patterns = ['123456', 'password', 'qwerty', 'abc123', 'letmein', 'password1']
        return any(pattern in self.password.lower() for pattern in common_patterns)

    def extract_advanced_features(self,wordlist: List[str] = None):
        if wordlist is None:
            wordlist = ['password', '123456', 'admin', 'welcome', 'dragon']  # Example default list

        return {
            "length": len(self.password),
            "has_upper": any(c.isupper() for c in self.password),
            "has_lower": any(c.islower() for c in self.password),
            "has_digit": any(c.isdigit() for c in self.password),
            "has_special": any(c in string.punctuation for c in self.password),
            "entropy": self.calculate_entropy(),
            "named_entity": len(self.check_semantics()) > 0,
            "password_reuse": self.check_password_reuse(self.password),
            "common_patterns": self.check_common_patterns(),
            "personal_info_leak": any(info.lower() in self.password.lower() for info in self.personal_info),
            "dictionary_word": self.check_dictionary(wordlist),
            "char_classes_count": sum([
                any(c.isupper() for c in self.password),
                any(c.islower() for c in self.password),
                any(c.isdigit() for c in self.password),
                any(c in string.punctuation for c in self.password)
            ])
        }
    def check_password_strength(self):
        features = self.extract_advanced_features()
        return features
