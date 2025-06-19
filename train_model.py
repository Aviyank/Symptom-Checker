import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib

# Load cleaned data
df = pd.read_csv('cleaned_data.csv')
X = df['symptoms']
y = df['disease']

# Build pipeline (optimized for speed and low memory)
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(max_features=500)),  # Limit features for speed/memory
    ('nb', MultinomialNB())
])

pipeline.fit(X, y)

# Save model
joblib.dump(pipeline, 'symptom_checker_model.joblib')
print('Model trained and saved as symptom_checker_model.joblib') 