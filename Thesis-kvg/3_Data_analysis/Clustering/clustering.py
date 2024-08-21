import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

cleaned_data = pd.read_excel('/Users/karsten/Downloads/Thesis/Cleaned data/Dataset_wihtout_stopwords_title.xlsx')

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(cleaned_data['cleaned_titles'])

pca = PCA(n_components=2, random_state=42)
X_reduced = pca.fit_transform(X.toarray())

num_clusters = 5  #number of clusters
kmeans = KMeans(n_clusters=num_clusters, random_state=42)
labels = kmeans.fit_predict(X_reduced)

cleaned_data['cluster'] = labels

clustered_file_path = '/Users/karsten/Downloads/Thesis/Cleaned data/Dataset_clustered_testing2.xlsx'
cleaned_data.to_excel(clustered_file_path, index=False)
