from flask import Flask, render_template, request
import pandas as pd
from recommendation import recommend
from popular_books import top_books

app = Flask(__name__)

data = pd.read_csv('famous_books.csv', index_col='Book-Title')
popular_books = pd.read_csv('most_popular.csv')

@app.route('/')
def home():
    return render_template('index.html')



@app.route('/recommendation', methods=['GET', 'POST'])
def get_recommendations():
    if request.method == 'POST':
        selected_book = request.form['book']
        recommendations = recommend(selected_book, data)
        selected_book_author = data.loc[selected_book, 'Book-Author']
        books_with_authors = [(book, data.loc[book, 'Book-Author']) for book in recommendations]
        book_titles = data.index.tolist()
        book_authors = data['Book-Author'].tolist()

        return render_template('recommendation.html', selected_book=selected_book, selected_book_author=selected_book_author,
                               recommendations=recommendations, books=books_with_authors, book_titles=book_titles, book_authors=book_authors)
    else:
        book_titles = data.index.tolist()
        book_authors = data['Book-Author'].tolist()
        return render_template('recommendation.html', book_titles=book_titles, book_authors=book_authors)

@app.route('/best_books', methods=['GET', 'POST'])
def best_books():
    n_books = 50  # Default value if the request method is not POST
    if request.method == 'POST':
        n_books = int(request.form['n'])

    popular = top_books(popular_books, n=n_books)
    popular.index = range(1, len(popular)+1)
    popular = popular.to_html()
    return render_template('best_books.html', popular=popular)

if __name__ == '__main__':
    app.run(debug=True)
