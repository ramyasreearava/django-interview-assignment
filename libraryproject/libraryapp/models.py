from django.db import models

class Librarian(models.Model):
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Username = models.CharField(max_length=60)
    Password = models.CharField(max_length=255)
    MobileNumber = models.CharField(max_length=14)
    objects = models.Manager

    class Meta:
        db_table = "Librarian-table"

# Create your models here.

class Member(models.Model):
    LibrarianId=models.ForeignKey('Librarian',on_delete=models.CASCADE,related_name='librarian')
    Firstname = models.CharField(max_length=30)
    Lastname = models.CharField(max_length=30)
    Email = models.EmailField(max_length=50)
    Username = models.CharField(max_length=60)
    Password = models.CharField(max_length=255)
    MobileNumber = models.CharField(max_length=14)

    objects = models.Manager

    class Meta:
        db_table = "Member-table"