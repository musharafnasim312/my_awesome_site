from django.db import models
from django.contrib.auth.models import User

class FavoriteThing(models.Model):
    CATEGORIES = [
        ('SONG', 'Cool Song'),
        ('GAME', 'Awesome Game'),
        ('MOVIE', 'Great Movie'),
    ]
    
    RATINGS = [
        (1, '⭐'),
        (2, '⭐⭐'),
        (3, '⭐⭐⭐'),
        (4, '⭐⭐⭐⭐'),
        (5, '⭐⭐⭐⭐⭐'),
    ]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=5, choices=CATEGORIES)
    why_awesome = models.TextField()
    image = models.ImageField(upload_to='favorite_things/', blank=True, null=True)
    rating = models.IntegerField(choices=RATINGS, default=3)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.get_category_display()}: {self.name}"
    
    def get_rating_stars(self):
        return self.get_rating_display()