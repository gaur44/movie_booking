from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'  # Change this in production

# MongoDB connection
client = MongoClient('mongodb://localhost:27017/')
db = client['movie_booking']
users_collection = db['users']

# Sample movie data
MOVIES_DATA = [
    {
        'id': 1,
        'title': 'The Matrix',
        'genre': 'Sci-Fi',
        'rating': '8.7',
        'duration': '136 min',
        'poster': 'https://placehold.co/300x450/000000/FFFFFF?text=The+Matrix'
    },
    {
        'id': 2,
        'title': 'Inception',
        'genre': 'Thriller',
        'rating': '8.8',
        'duration': '148 min',
        'poster': 'https://placehold.co/300x450/1a1a1a/FFFFFF?text=Inception'
    },
    {
        'id': 3,
        'title': 'Interstellar',
        'genre': 'Drama',
        'rating': '8.6',
        'duration': '169 min',
        'poster': 'https://placehold.co/300x450/2a2a2a/FFFFFF?text=Interstellar'
    },
    {
        'id': 4,
        'title': 'The Dark Knight',
        'genre': 'Action',
        'rating': '9.0',
        'duration': '152 min',
        'poster': 'https://placehold.co/300x450/3a3a3a/FFFFFF?text=Dark+Knight'
    }
]

@app.route('/')
def index():
    if 'user_id' in session:
        return render_template('movies.html', movies=MOVIES_DATA, username=session['username'])
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        
        user = users_collection.find_one({'email': email})
        
        if user and check_password_hash(user['password'], password):
            session['user_id'] = str(user['_id'])
            session['username'] = user['username']
            return redirect(url_for('movies'))
        else:
            flash('Invalid email or password')
    
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        
        if users_collection.find_one({'email': email}):
            flash('Email already exists')
        else:
            hashed_password = generate_password_hash(password)
            users_collection.insert_one({
                'username': username,
                'email': email,
                'password': hashed_password
            })
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/movies')
def movies():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    return render_template('movies.html', movies=MOVIES_DATA, username=session['username'])

@app.route('/book/<int:movie_id>')
def book_movie(movie_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    movie = next((m for m in MOVIES_DATA if m['id'] == movie_id), None)
    if movie:
        return render_template('booking.html', movie=movie)
    return redirect(url_for('movies'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)