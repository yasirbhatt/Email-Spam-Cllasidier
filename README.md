# Email-Spam-Cllasidier
## Email Spam Classifier - GitHub Project Files

### 1. Folder Structure:
```
email-spam-classifier/
├── README.md
├── spam_classifier.ipynb
├── vectorizer.pkl
├── naive_bayes_model.pkl
├── requirements.txt
└── sample_email_test.py
```

### 2. README.md
```markdown
# 📧 Email Spam Classifier using Machine Learning

This project detects whether an email is spam or not using machine learning techniques.

## 🔧 Tools & Libraries
- Python
- Pandas, Matplotlib, Seaborn
- Scikit-learn (MultinomialNB, DecisionTreeClassifier)
- CountVectorizer (for feature extraction)
- Joblib (for model saving)

## 🚀 Features
- Achieved **97.9% accuracy** with Multinomial Naive Bayes
- Outperformed Decision Tree (J48-style) model
- Applied **5-fold cross-validation** with **98.05% mean accuracy**
- Integrated real-time prediction for new email input
- Model and vectorizer saved using `joblib` for deployment

## 📌 Example
```python
input_mail = ["Congratulations! You've won a prize! Click here..."]
features = vectorizer.transform(input_mail)
prediction = model.predict(features)
```

## 📂 Outputs
- `naive_bayes_model.pkl`
- `vectorizer.pkl`
```

### 3. requirements.txt
```
pandas
numpy
scikit-learn
matplotlib
seaborn
joblib
```

### 4. sample_email_test.py
```python
import joblib

# Load model and vectorizer
model = joblib.load('naive_bayes_model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

# Input email
input_mail = ["Congratulations! You've won a free iPhone. Click here now!"]
features = vectorizer.transform(input_mail)
prediction = model.predict(features)

if prediction[0] == 1:
    print("Ham email")
else:
    print("Be careful, this is a SPAM email")
```

### 5. spam_classifier.ipynb
> (Upload your full Jupyter notebook here with all code, outputs, and visualizations.)
