import math

# Define the corpus of documents
corpus = [
    "I'd like an apple.",
    "An apple a day keeps the doctor away.",
    "Never compare an apple to an orange.",
    "I prefer scikit-learn to orange."
]

# Function to calculate term frequency
def term_frequency(document):
    words = document.split()
    word_count = len(words)
    term_freq = {}
    for word in words:
        term_freq[word] = term_freq.get(word, 0) + 1
    for word in term_freq:
        term_freq[word] /= word_count
    return term_freq

# Function to calculate inverse document frequency
def inverse_document_frequency(corpus):
    idf = {}
    num_documents = len(corpus)
    for document in corpus:
        words = set(document.split())
        for word in words:
            idf[word] = idf.get(word, 0) + 1
    for word in idf:
        idf[word] = math.log(num_documents / idf[word])
    return idf

# Function to calculate TF-IDF score
def tfidf(document, idf):
    tf = term_frequency(document)
    tfidf_scores = {}
    for word in tf:
        tfidf_scores[word] = tf[word] * idf.get(word, 0)
    return tfidf_scores

# Compute IDF for the corpus
idf_scores = inverse_document_frequency(corpus)

# Compute TF-IDF scores for all documents
tfidf_matrix = []
for document in corpus:
    tfidf_matrix.append(tfidf(document, idf_scores))

# Compute cosine similarity between the first document and all other documents
cosine_similarities = []
for i in range(1, len(tfidf_matrix)):
    dot_product = sum(tfidf_matrix[0][word] * tfidf_matrix[i][word] for word in tfidf_matrix[0] if word in tfidf_matrix[i])
    norm_first = math.sqrt(sum(tfidf_matrix[0][word] ** 2 for word in tfidf_matrix[0]))
    norm_other = math.sqrt(sum(tfidf_matrix[i][word] ** 2 for word in tfidf_matrix[i]))
    cosine_similarities.append(dot_product / (norm_first * norm_other))

# Find the index of the document with the highest similarity
most_similar_index = cosine_similarities.index(max(cosine_similarities)) + 2  # Adding 2 to convert 0-indexed to 1-indexed

# Output the identifier of the most similar document
print(most_similar_index)
