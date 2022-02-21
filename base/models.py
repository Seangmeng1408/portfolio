from distutils.command.upload import upload
from email.policy import default
from tkinter import READABLE
from turtle import back
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.
class Achievment(models.Model):
    project=models.CharField(max_length=200)
    describe=RichTextUploadingField(null=True,blank=True)
    thumnail=models.ImageField(null=True,blank=True,upload_to="images",default="default-thumbnail.jpg")
    isComplete=models.BooleanField(default=False)
    Readable=models.BooleanField(default=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(null=True,blank=True)
    liveUrl=models.CharField(max_length=200,blank=True)
    sourceUrl=models.CharField(max_length=200,blank=True)
    def __str__(self):
        return self.project
    def save(self,*args,**kwargs):

        if self.slug==None:
            slug=slugify(self.project)
            has_slug=Achievment.objects.filter(slug=slug).exists()
            count=1
            while has_slug:
                count+=1
                slug=slugify(self.project)+'-'+str(count)
                has_slug=Achievment.objects.filter(slug=slug).exists()
            self.slug=slug
        super().save(*args,**kwargs)