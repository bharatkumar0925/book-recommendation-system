from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import numpy as np

def recommend(book_title, data, top_n=10):
    data = data.iloc[:, :-1]
#    data.drop('Book-Author', axis=1, inplace=True)
    # Get the index of the book title
    book_index = np.where(data.index == book_title)[0][0]

    # Calculate cosine similarity scores
    scores = cosine_similarity([data.iloc[book_index]], data)[0]

    # Get indices of top n similar books
    top_indices = np.argsort(scores)[::-1][1:top_n+1]  # Exclude the book itself

    # Get the titles of top n similar books
    top_books = data.iloc[top_indices].index.tolist()

    return top_books
