# 🎬 MovieFlix - Movie Booking Website

A modern, responsive movie booking website built with Flask and MongoDB featuring secure user authentication and a clean, intuitive interface.

## ✨ Features

- 🔐 **Secure User Authentication** - Registration and login with hashed passwords
- 🎭 **Movie Catalog** - Browse movies with detailed information and ratings
- 📱 **Responsive Design** - Works seamlessly on desktop, tablet, and mobile
- 🎨 **Modern UI/UX** - Glass morphism effects, smooth animations, and intuitive navigation
- 🛡️ **Security First** - Session management, password hashing, and protected routes
- 🗄️ **NoSQL Database** - MongoDB for scalable data storage

## 📋 Prerequisites

- **Python 3.7+** installed
- **MongoDB** Community Server running locally
- **pip** package manager

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd movie_booking
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start MongoDB**
   ```bash
   # On Windows
   net start MongoDB
   
   # On macOS (with Homebrew)
   brew services start mongodb-community
   
   # On Linux
   sudo systemctl start mongod
   ```

## ▶️ Running the Application

1. **Run the Flask app**
   ```bash
   python app.py
   ```

2. **Access the website**
   
   Open your browser and navigate to: `http://localhost:5000`

## 🏗️ Project Structure

```
movie_booking/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
└── templates/            # Jinja2 templates
    ├── base.html         # Master template with navigation
    ├── login.html        # User login form
    ├── register.html     # User registration form
    ├── movies.html       # Movie catalog page
    └── booking.html      # Booking placeholder page
```

## 🛠️ Technology Stack

### Backend
- **Flask 2.3.3** - Lightweight web framework
- **PyMongo 4.5.0** - MongoDB driver for Python
- **Werkzeug 2.3.7** - Password hashing and security utilities

### Frontend
- **HTML5** - Semantic markup
- **CSS3** - Modern styling with Flexbox and Grid
- **JavaScript** - Enhanced user interactions
- **Jinja2** - Server-side templating

### Database
- **MongoDB** - Document-oriented NoSQL database
