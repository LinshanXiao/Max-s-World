from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

# Function to retrieve movies by category from the database
def get_movies_by_category(category_id):
    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM movies WHERE category_id = ?", (category_id,))
    movies = cursor.fetchall()
    conn.close()
    return movies

# Home page route
@app.route('/')
def home():
    return render_template('home.html')

# Category page route
@app.route('/category/<int:category_id>')
def category(category_id):
    movies = get_movies_by_category(category_id)
    return render_template('category.html', movies=movies)

if __name__ == '__main__':
    app.run(debug=True)