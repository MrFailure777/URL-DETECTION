from flask import Flask, render_template, request
import pickle
import tldextract

app = Flask(__name__)

# Load model
model = pickle.load(open("model.pkl", "rb"))

# Feature extraction function
def extract_features(url):
    extracted = tldextract.extract(url)
    return [
        len(url),
        sum(c.isdigit() for c in url),
        sum(c in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for c in url),
        hash(extracted.domain) % 1000,
        hash(extracted.suffix) % 1000,
        hash(extracted.subdomain) % 1000
    ]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    url = request.form['url_input']
    features = extract_features(url)
    prediction = model.predict([features])
    result = "Malicious" if prediction[0] == 1 else "Safe"
    return render_template('index.html', prediction_text=f"Result: {result}")

if __name__ == '__main__':
    app.run(debug=True)
