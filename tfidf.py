from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import pairwise_kernels
from nltk.corpus import stopwords
import generate_html
import numpy as np
import load_data
import time


# Load data
data = load_data.load()
data = data.drop(['TYPE', 'YEAR', 'EXHIBITION', 'TAGS'], axis=1)

# Initialize variables
corpus = []

# Union of title subtitle and description in a single corpus
for i, obj in data.iterrows():
    # s = ['TITLE: ', obj['TITLE'], ' | SUBTITLE: ', obj['SUBTITLE'], ' | DESCRIPTION: ', obj['DESC']]
    s = obj['TITLE'] + ' ' + obj['SUBTITLE'] + ' ' + obj['DESC']
    corpus.append(obj['DESC'])

# Calculate TF-IDF and add in a pandas df
vectorizer = TfidfVectorizer(stop_words=stopwords.words('english'))
X = vectorizer.fit_transform(corpus)
cosine = pairwise_kernels(X, metric='cosine')

new_data_column = []
for i in range(0, X.shape[0]):
    # Find the 5 maximum values in the matrix row array
    ind = np.argpartition(cosine[i], -5)[-6:]

    # Sort values from smallest to biggest
    sorted_indexes = ind[np.argsort(cosine[i][ind])]

    # Reverse the order
    most_similar_indexes = list(reversed(sorted_indexes))

    # Find correct IDs of the objects
    most_similar_ids = [x+1 for x in most_similar_indexes]

    if data.loc[i]['ID'] in most_similar_ids:
        most_similar_ids.remove(data.loc[i]['ID'])

    # Append the data to a list
    new_data_column.append(most_similar_ids)

data['SIMILAR ARTS'] = new_data_column

# Results for Philip Tan selected arts
generate_html.similar_items(data, 86, 'Philip Tan - TFIDF - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 41, 'Philip Tan - TFIDF - Black and White Image')

# Results for Michael Sta. Maria selected arts
time.sleep(2)
generate_html.similar_items(data, 130, 'Michael Sta. M. - TFIDF - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 138, 'Michael Sta. M. - TFIDF - Black and White Image')

# Results for Diogo Ferreira selected arts
time.sleep(2)
generate_html.similar_items(data, 0, 'Diogo Ferreira - TFIDF - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 10, 'Diogo Ferreira - TFIDF - Black and White Image')

# Results for Jim Lee selected arts
time.sleep(2)
generate_html.similar_items(data, 240, 'Jim Lee - TFIDF - Colored Image')
time.sleep(2)
generate_html.similar_items(data, 181, 'Jim Lee - TFIDF - Black and White Image')
