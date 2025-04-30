# My Awesome Collection

A Django web application for managing and showcasing your favorite things - including songs, games, and movies! Perfect for keeping track of your entertainment favorites with ratings, descriptions, and images.

## Features

- **User Authentication**: Secure login and signup system
- **Personal Collection Management**:
  - Add, edit, and delete your favorite items
  - Categorize items as Songs, Games, or Movies
  - Rate items with a 5-star system (⭐ to ⭐⭐⭐⭐⭐)
  - Add personal notes about why you love each item
  - Upload images for visual representation
- **Interactive Dashboard**:
  - View all your favorites in one place
  - Filter by category
  - Sort by rating or date added
  - Search functionality

## Use Cases

1. **Personal Entertainment Tracker**:
   - Keep track of games you want to play
   - Remember great movies you've watched
   - Create your ultimate song playlist

2. **Recommendation System**:
   - Share your top-rated items with friends
   - Keep notes on why you loved certain items
   - Build a personal entertainment database

3. **Memory Journal**:
   - Document your entertainment journey
   - Record your thoughts and feelings about each item
   - Track how your tastes change over time

## Tech Stack

- **Backend**: Python 3.x with Django 5.0.2
- **Database**: SQLite3 (default)
- **Image Processing**: Pillow 10.2.0
- **Environment Management**: python-dotenv 1.0.1
- **Frontend**: Bootstrap 5 for responsive design

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/my_awesome_site.git
cd my_awesome_site
```

2. Create and activate virtual environment:
```bash
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment:
- Create `.env` file in root directory
- Add required environment variables:
  ```
  SECRET_KEY=your_secret_key_here
  DEBUG=True
  ```

5. Setup database:
```bash
python manage.py migrate
```

6. Create admin user (optional):
```bash
python manage.py createsuperuser
```

7. Start development server:
```bash
python manage.py runserver
```

Access the application at http://127.0.0.1:8000

## Project Structure

```
my_awesome_site/
├── mycollection/          # Main Django app
│   ├── favorites/        # Favorites management app
│   │   ├── models.py    # Data models
│   │   ├── views.py     # View logic
│   │   └── templates/   # HTML templates
├── requirements.txt      # Project dependencies
├── .env                 # Environment variables
└── README.md           # Project documentation
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

This project is licensed under the MIT License.
