import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Ingestion
df = pd.read_csv("raw_skills.csv")

print("=== DecodeLabs Tech Stack Recommender ===")
user_skills = []
for i in range(1, 4):
    skill = input(f"Enter skill/preference {i}: ").strip()
    if skill:
        user_skills.append(skill)

user_profile = " ".join(user_skills)

# Step 2: Scoring (TF-IDF & Cosine Similarity Engine)
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['Skills'])
user_vector = tfidf.transform([user_profile])

df['Similarity_Score'] = cosine_similarity(user_vector, tfidf_matrix).flatten()

# Step 3: Sorting & Step 4: Filtering (Top-3 Output)
recommendations = df.sort_values(by='Similarity_Score', ascending=False).head(3)

print("\n--- Recommended Career Paths ---")
for idx, row in recommendations.iterrows():
    match_pct = round(row['Similarity_Score'] * 100, 1)
    print(f"Role: {row['Job_Role']} | Match: {match_pct}%")
    print(f"Required Skills: {row['Skills']}\n")