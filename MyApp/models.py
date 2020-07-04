from django.db import models

# Create your models here.
class Course(models.Model):
    course_id = models.AutoField(primary_key= True)
    course_title  =models.CharField(max_length=100, default="")
    course_desc = models.CharField(max_length=1000, default="")
    course_outline = models.CharField(max_length=2000,default="")
    course_fee = models.IntegerField(default=0)
    course_img = models.ImageField(upload_to='MyApp/images',default="")

class Candidiates(models.Model):
    candidiate_id  = models.AutoField(primary_key=True)
    candidiate_name = models.CharField(max_length=100,default="")
    candidiate_email = models.CharField(max_length=50, default="")
    candidiate_number  =models.IntegerField(default=0)
    candidiate_city = models.CharField(max_length=50,default="")
    course_id = models.IntegerField()

class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_name = models.CharField(max_length=50)
    review_email = models.CharField(max_length=30, default="")
    review = models.CharField(max_length=1000, default="")
    review_date  = models.DateField(auto_now_add=True)
    hide_review = models.CharField(max_length=10, default="")
    def __str__(self):
        return self.review_email