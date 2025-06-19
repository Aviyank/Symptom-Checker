# 🩺 Smart Health Symptom Checker

A lightweight, ML-powered web app to predict possible diseases based on user-entered symptoms. Built with Python, scikit-learn, and Streamlit. Optimized for CPU/RAM and deployable on Hugging Face Spaces.

## 🚀 Features
- **Input:** User enters symptoms (comma-separated, e.g., `fever, cough`)
- **ML Model:** Naive Bayes + TF-IDF classifier trained on a Kaggle disease-symptoms dataset
- **Output:** Predicts likely conditions with confidence scores
- **UI:** Clean, interactive Streamlit interface
- **Deployment:** Runs locally or on Hugging Face Spaces

## 📦 Files
- `app.py` — Streamlit web app
- `prepare_data.py` — Data cleaning/preparation script
- `train_model.py` — Model training script
- `dataset.csv` — Raw Kaggle dataset
- `cleaned_data.csv` — Cleaned data for training
- `symptom_checker_model.joblib` — Trained model
- `requirements.txt` — Python dependencies

## 🛠️ Setup & Usage
1. **Clone the repo:**
   ```bash
   git clone https://github.com/Aviyank/Symptom-Checker.git
   cd Symptom-Checker
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Prepare data & train model (if needed):**
   ```bash
   python prepare_data.py
   python train_model.py
   ```
4. **Run the app locally:**
   ```bash
   streamlit run app.py
   ```

## 🌐 Deploy on Hugging Face Spaces
- Upload all files to a new Space (Streamlit type)
- Ensure `requirements.txt` is present
- App will launch automatically

## ⚠️ Disclaimer
This tool is for educational purposes only and is **not** a substitute for professional medical advice, diagnosis, or treatment.

---
Created with ❤️ by [Aviyank](https://github.com/Aviyank)
