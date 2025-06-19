import streamlit as st
import joblib
import re

# --- Sidebar ---
st.sidebar.title('🩺 Smart Health Symptom Checker')
st.sidebar.markdown('''
**How it works:**
- Enter your symptoms (comma-separated)
- The app predicts the most likely disease
- Shows top 3 predictions with confidence

*Powered by Naive Bayes & TF-IDF*  
*Optimized for CPU/RAM*  
''')
st.sidebar.info('For educational purposes only. Not a substitute for professional medical advice.')

# --- Main UI ---
st.title('🩺 Smart Health Symptom Checker')
st.markdown('''
Enter your symptoms below (e.g., `fever, cough, headache`).

:bulb: *Separate each symptom with a comma.*
''')

# --- Input and Prediction ---
col1, col2 = st.columns([3, 2])
with col1:
    user_input = st.text_input('Symptoms:', placeholder='e.g. fever, cough, headache')
with col2:
    st.image('https://cdn-icons-png.flaticon.com/512/2966/2966484.png', width=80)

def clean_symptom_text(text):
    text = text.lower()
    text = text.replace('_', ' ')
    text = re.sub(r'[^a-zA-Z0-9, ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Load model
model = joblib.load('symptom_checker_model.joblib')

if st.button('🔍 Check My Symptoms'):
    cleaned = clean_symptom_text(user_input)
    if cleaned:
        pred_proba = model.predict_proba([cleaned])[0]
        pred_class = model.classes_[pred_proba.argmax()]
        confidence = pred_proba.max() * 100
        st.success(f'**Prediction:** {pred_class} ({confidence:.1f}% confidence)')
        # Show top 3 predictions
        top_indices = pred_proba.argsort()[-3:][::-1]
        st.markdown('---')
        st.subheader('Top 3 Possible Conditions:')
        for idx in top_indices:
            st.write(f"- **{model.classes_[idx]}**: {pred_proba[idx]*100:.1f}%")
    else:
        st.warning('Please enter at least one symptom.')

st.markdown('---')
st.caption('Created with ❤️ using Streamlit | [GitHub](https://github.com/)') 