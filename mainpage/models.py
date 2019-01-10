from django.db import models

# Create your models here.


class Works(models.Model):

    Digital = 'Digital'
    Traditional = 'Traditional'
    medium_choices = ((Digital, 'Digital'), (Traditional, 'Traditional'))
    title = models.CharField(max_length=255)
    art = models.ImageField()
    about = models.TextField()
    medium = models.CharField(max_length=50, choices=medium_choices, default=Traditional)
    details = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Works"

    def __str__(self):
        return self.title


# class Buyer(models.Model):
#     # India = "India"
#     # choice = ((India,'India'))
#     firstname = models.CharField(max_length=100)
#     lastname = models.CharField(max_length=100)
#     email = models.EmailField()
#     address = models.CharField(max_length=300)
#     zipcode = models.IntegerField(max_digits=8)
    # country=models.CharField(max_length=20, choices=choice, default=India )
