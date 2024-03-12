from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class User(User):
    options = (
        ("user", "user"),
        ("mechanic", "mechanic")
    )
    user_type = models.CharField(max_length=200, choices=options, default="user")


class Location(models.Model):
    name=models.CharField(max_length=200)

    def _str_(self):
        return self.name
  
class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="user_profile")
    address=models.CharField(max_length=200)
    phone=models.CharField(max_length=200)
    dob=models.DateField(null=True)
    bio=models.CharField(max_length=200)
    profile_pic=models.ImageField(null=True,upload_to="images\profile_img")
    
    def _str_(self):
        return self.user.username
    
class MechanicProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE,related_name="mechanic_profile")
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name="mechanic_location")
    phone=models.CharField(max_length=200)
    dob=models.DateField(null=True)
    skills=models.CharField(max_length=200)
    experience=models.CharField(max_length=200)
    is_approved=models.CharField(max_length=200)
    options=(
        ("two_wheeler","two_wheeler"),
        ("four_wheeler","four_wheeler"),
        ("heavy_vehicle","heavy_vehicle"),
    )
    specialized_in=models.CharField(max_length=200,choices=options)
    bio=models.CharField(max_length=200)
    profile_pic=models.ImageField(null=True,upload_to="images\profile_img")
    
    def _str_(self):
        return self.user.username
    
class FeedBack(models.Model):
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="feedback_userprofile")
    mechanic=models.ForeignKey(MechanicProfile,on_delete=models.CASCADE,related_name="feedback_mechanicprofile")
    text=models.CharField(max_length=200)
    total_bill=models.IntegerField()
    options=(
        ("1","1"),
        ("2","2"),
        ("3","3"),
        ("4","4"),
        ("5","5"),
    )
    rating=models.CharField(max_length=200,choices=options,default="5")

class RentCar(models.Model):
    name=models.CharField(max_length=200)
    day_rent=models.IntegerField()
    week_rent=models.IntegerField()
    month_rent=models.IntegerField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name="rent_car_location")
    car_img=models.ImageField(null=True,upload_to="images\car_img")
    discription=models.CharField(max_length=200)
    
    def _str_(self):
        return self.name

class ReqToMechanic(models.Model):
    
    user=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="req_profile")
    mechanic=models.ForeignKey(MechanicProfile,on_delete=models.CASCADE,related_name="req_profile")
    discription=models.CharField(max_length=200)
    phone=models.IntegerField()
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name="req_location")

    
