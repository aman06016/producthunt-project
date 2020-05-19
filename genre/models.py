from django.db import models

class Genre(models.Model):
    title=models.CharField(max_length=50)
    covers=models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.title
