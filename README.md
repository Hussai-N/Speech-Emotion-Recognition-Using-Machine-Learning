# 🎙️ Speech Emotion Recognition using Machine Learning

## 📌 Project Overview
This project focuses on classifying emotions from speech audio files using machine learning techniques. Audio features such as MFCC (Mel-Frequency Cepstral Coefficients) are extracted and used to train a classification model. The goal is to predict the underlying emotion expressed in the speech.

## 📂 Dataset
The dataset contains audio recordings labeled with emotions such as:
- Happy
- Sad
- Angry
- Neutral
- Fearful
- Disgust
- Surprised

### 🎧 Features Extracted
- MFCCs (Mel-Frequency Cepstral Coefficients) - 13 coefficients per sample
- (Optional) Chroma, Mel Spectrogram, Zero-Crossing Rate

---

## 📊 Model Used
- Logistic Regression (Baseline Model)
- Support Vector Machine (SVM) (Tuned using GridSearchCV)

---

## 🏗️ Project Workflow
1. Data Preprocessing: Load audio files, extract features.
2. Split Data: Divide into train and test sets.
3. Model Training: Train Logistic Regression / SVM.
4. Model Evaluation: Evaluate using:
   - Classification Report
   - Confusion Matrix
   - Cross-validation scores
5. Model Saving: Save trained model using `joblib`.
6. Model Testing: Test saved model on new samples.

---

## 📈 Performance Metrics
| Metric          | Value |
|------------------|------|
| **Accuracy**    | 41% |
| **Macro F1-score** | 39% |
| **Cross-validation Accuracy** | ~41% |

### 🚨 Note
- Accuracy is currently low due to limited features & noise.
- Can improve with better features and deep learning models (CNN, LSTM).
