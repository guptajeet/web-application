from django.db import models


# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):
        return self.name + " - " + self.email


class Blog(models.Model):
    sno = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    desc = models.CharField(max_length=300, default="")
    slug = models.CharField(max_length=100)
    time = models.DateTimeField(auto_now_add=True)
    #time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Books(models.Model):
    bname = models.CharField(max_length=20)
    bdesc = models.CharField(max_length=250)
    bauthor= models.CharField(max_length=40)
    emailid = models.EmailField()

    class Meta:
        db_table = "books"

    def __str__(self):
        return self.bname
