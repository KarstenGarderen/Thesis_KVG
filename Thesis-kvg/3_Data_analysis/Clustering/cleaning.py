import pandas as pd
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
import re

data = pd.read_excel('/Users/karsten/Downloads/Thesis/Results/Body_clustering.xlsx')

# Specify the path to  NLTK data
nltk.data.path.append('/Users/karsten/Downloads/stopwords/english')

def preprocess_text(text):
    if not isinstance(text, str):
        text = ''
    text = re.sub(r'\W', ' ', text)  
    text = re.sub(r'\s+', ' ', text) 
    text = text.lower()  
    tokens = text.split()  
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english')] 
    return ' '.join(tokens)

data['cleaned_body'] = data['body'].apply(preprocess_text)

cleaned_file_path = '/Users/karsten/Downloads/Thesis/Cleaned data/body_without_stopwords.xlsx'
data.to_excel(cleaned_file_path, index=False)
