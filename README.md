# 🛡️ Phishing URL Detection using Machine Learning

This project aims to detect whether a given URL is legitimate or a phishing attempt using machine learning techniques. It leverages various features extracted from URLs to train a classification model that identifies malicious links.

## 🚀 Features

- ✅ URL classification as "Legitimate" or "Phishing"
- 📊 Uses machine learning models like Random Forest or Logistic Regression
- 🌐 Web interface for testing URLs
- 🔒 Designed to help users avoid malicious links

## 🛠️ Tech Stack

- **Python**: Core language
- **scikit-learn**: For building ML models
- **Pandas / NumPy**: For data preprocessing
- **Flask / Streamlit**: For web app interface
- **HTML/CSS**: For front-end styling

## 📂 Dataset

The dataset used includes a variety of features extracted from URLs (length, presence of “@”, IP usage, etc.), labeled as phishing or legitimate. Source: [Phishing Websites Dataset](https://www.kaggle.com/datasets)

## ⚙️ How to Run

```bash
# Clone the repository
git clone https://github.com/yourusername/phishing-url-detector.git
cd phishing-url-detector

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
