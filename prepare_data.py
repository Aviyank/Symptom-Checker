import pandas as pd
import re

# Data cleaning function
def clean_symptom_text(text):
    if not isinstance(text, str):
        return ''
    text = text.lower()
    text = text.replace('_', ' ')
    text = re.sub(r'[^a-zA-Z0-9, ]', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

# Load dataset
df = pd.read_csv('dataset.csv')

# Combine all symptom columns into one string per row
symptom_cols = [col for col in df.columns if col.startswith('Symptom')]
def combine_symptoms(row):
    symptoms = [str(row[col]).strip() for col in symptom_cols if pd.notnull(row[col]) and str(row[col]).strip() != '']
    return ', '.join(symptoms)

df['all_symptoms'] = df.apply(combine_symptoms, axis=1)
df['all_symptoms_clean'] = df['all_symptoms'].apply(clean_symptom_text)

# Keep only necessary columns
df_clean = df[['Disease', 'all_symptoms_clean']].rename(columns={'Disease': 'disease', 'all_symptoms_clean': 'symptoms'})

# Save cleaned data
df_clean.to_csv('cleaned_data.csv', index=False)

print('Cleaned data saved to cleaned_data.csv') 