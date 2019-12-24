from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=264)
    last_name = models.CharField(max_length=264)
    email = models.EmailField(max_length=70, unique=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.email