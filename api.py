from flask import Flask, request, jsonify
from password_classifier import PasswordClassifier
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

classifier = PasswordClassifier(model_path="mmmodel.pkl")  # adjust the path as needed

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    password = data.get('password', '')
    personal_info = data.get('personal_info', '')

    # The classifier uses the custom prediction method
    prediction = classifier.predict_strength(password, [personal_info])

    return jsonify({'prediction': prediction})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
