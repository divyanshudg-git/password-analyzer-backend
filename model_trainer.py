import pickle
from sklearn.ensemble import HistGradientBoostingClassifier
from AdvancedPasswordAnalyzer import AdvancedPasswordAnalyzer
import random
import string

def generate_random_password(length=16):
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

def generate_training_data():
    X = []
    y = []
    
    weak_passwords = [
        '123456', 'password', 'qwerty', 'abc123', 'letmein',
        'iloveyou', 'monkey', 'football', 'admin', 'welcome',
        'passw0rd', '12345678', '123123', 'superman'
    ]
    
    strong_passwords = [generate_random_password(16) for _ in range(50)]
    
    personal_info = ["john", "doe", "birthday", "company"]
    
    all_passwords = weak_passwords + strong_passwords
    
    for pwd in all_passwords:
        analyzer = AdvancedPasswordAnalyzer(pwd, personal_info)
        features = analyzer.extract_advanced_features()

        total_entropy = features['entropy'] * len(pwd)
        
        # Check the correct feature names and use them accordingly
        label = 1 if (
            total_entropy >= 60 and
            features['char_classes_count'] >= 3 and  # Check if 'char_classes_count' is correct
            not features['personal_info_match'] and
            not features['common_patterns'] and
            not features['repetition_detected'] and
            not features['keyboard_pattern']
        ) else 0
        
        processed_features = [int(v) if isinstance(v, bool) else v for v in features.values()]
        
        X.append(processed_features)
        y.append(label)
    
    return X, y

def main():
    X, y = generate_training_data()
    
    print(f"Generated {len(X)} samples with {len(X[0])} features each")
    print(f"Class distribution: {y.count(0)} weak, {y.count(1)} strong")

    clf = HistGradientBoostingClassifier(max_iter=200, random_state=42, verbose=1)
    clf.fit(X, y)
    
    with open('mmmodel.pkl', 'wb') as f:
        pickle.dump(clf, f, protocol=pickle.HIGHEST_PROTOCOL)

    print("Model saved as mmmodel.pkl")

if __name__ == "__main__":
    main()
