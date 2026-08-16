from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BookList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    publication_date = models.DateTimeField()
    
    def __str__(self):
        return self.title
    
    
class Review(models.Model):
    booklist = models.ForeignKey(BookList, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField()
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Review by {self.reviewer} given {self.rating} stars"
    
    
