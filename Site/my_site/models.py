from django.db import models
from autoslug import AutoSlugField
from taggit.managers import TaggableManager
from django.urls import reverse
from ckeditor_uploader.fields import RichTextUploadingField
from ckeditor.fields import RichTextField

class SignsList(models.Model):
    Title = models.TextField(blank=True )
    Image = models.TextField(blank=True)
    Daily = models.TextField(blank=True,null=True)
    Love = models.TextField(blank=True, null=True)
    Finance = models.TextField(blank=True, null=True)
    date = models.DateField(auto_now=True)


    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("singCategory", args=[self.Title, "Daily"]) or reverse("singCategory", args=[self.Title, "Love"])


##editable=False


class Blogmodel(models.Model):
    Title = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="images/",null=True)
    body = RichTextUploadingField(blank=True, null=True)
    slug = models.TextField()
    publish = models.DateField(auto_now=False, auto_now_add=False,null=True)
    tags = models.TextField(blank=True, null=True)
    hits=models.IntegerField(default=0)


    def __str__(self):
        return self.Title

    def get_absolute_url(self):
        return reverse("blogDetail", kwargs={"slug": self.slug})
    
    


    
    
