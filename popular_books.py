import pandas as pd
import numpy as np



def top_books(books, n=20):
    books['AVG_Rating'] = books['AVG_Rating'].round(2)
    books['Rank1'] = books['Total_Rating'].rank(method='min', ascending=True)
    books['Rank2'] = books['Rating_Count'].rank(method='min', ascending=True)
    books['Rank3'] = books['AVG_Rating'].rank(method='min', ascending=True)
    books['Rank4'] = books['Year-Of-Publication'].rank(method='min', ascending=True)
    books['Score'] = (books['Rank1']*0.35+books['Rank2']*0.35+books['Rank3']*0.1+books['Rank4']*0.2)
    books = books.sort_values(by='Score', ascending=False).reset_index(drop=True)
    books.drop(['Rank1', 'Rank2', 'Rank3', 'Rank4', 'Score'], axis=1, inplace=True)
    return books.iloc[:n, :]


data = pd.read_csv('most_popular.csv')

top = top_books(data, n=50)
print(top.to_string())
