from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255)
    pic = models.ImageField()
    content = models.TextField()
    postdate = models.DateTimeField(auto_now=False,auto_now_add=True)
    editdate = models.DateTimeField(auto_now=True,auto_now_add=False)


    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Posts"
