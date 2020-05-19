from django.db import models

# Create your models here.
class Selfhelp(models.Model):
    book_name=models.CharField(max_length=40)
    author = models.CharField(max_length=30)
    date= models.DateField(auto_now=False,auto_now_add=False)
    genre=models.CharField(max_length=40)
    pages=models.IntegerField()
    rating=models.FloatField()
    summary=models.TextField(max_length=5000)
    Book_cover=models.ImageField(upload_to='images/')

    def __str__(self):
        return self.book_name
