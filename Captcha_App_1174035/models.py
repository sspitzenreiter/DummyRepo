from django.db import models

# Create your models here.
class User(models.Model):
    

    username = models.CharField(max_length=128)
    nickname = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    confirm_password = models.CharField(max_length=128)
    email = models.EmailField(max_length=254,unique=True)
    namarek = models.CharField(max_length=128)
    norek = models.CharField(max_length=128)
    nama_bank = models.CharField(max_length=128 )
    ref = models.CharField(max_length=128)

    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name_plural = "User"
