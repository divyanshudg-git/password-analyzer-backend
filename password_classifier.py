import pickle
import numpy as np
from AdvancedPasswordAnalyzer import AdvancedPasswordAnalyzer

class PasswordClassifier:
    def __init__(self, model_path="/Users/divyanshaggarwal/Desktop/SE/mmmodel.pkl"):
        self.model = self.load_model(model_path)

    def load_model(self, path: str):
        with open(path, 'rb') as f:
            return pickle.load(f)

    def predict_strength(self, password: str, personal_info: list):
        analyzer = AdvancedPasswordAnalyzer(password, personal_info)
        features = analyzer.extract_advanced_features()

        # Convert boolean features to integers
        processed_features = [int(v) if isinstance(v, bool) else v for v in features.values()]

        feature_vector = np.array([processed_features])
        prediction = self.model.predict(feature_vector)[0]

        return "Strong" if prediction == 1 else "Weak"


