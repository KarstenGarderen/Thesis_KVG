import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import numpy as np


cleaned_data = pd.read_excel('/Users/karsten/Downloads/Thesis/Cleaned data/body_without_stopwords.xlsx')

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_data['cleaned_body'])

num_clusters = 6

kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(X)

cleaned_data['cluster'] = labels

def get_top_keywords(data, labels, vectorizer, n_terms):
    df = pd.DataFrame(data.todense()).groupby(labels).mean()
    terms = vectorizer.get_feature_names_out()
    keywords = []
    for i, r in df.iterrows():
        keywords.append([terms[t] for t in np.argsort(r)[-n_terms:]])
    return keywords

n_terms = 20  
top_keywords = get_top_keywords(X, labels, vectorizer, n_terms)

for i in range(num_clusters):
    print(f"Cluster {i}: {', '.join(top_keywords[i])}")

