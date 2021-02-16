from django.db import models


# Create your models here.
#PROFILE
class profile(models.Model):
    user_id=models.CharField(max_length=20)
    mobile_no=models.CharField(max_length=20)
    alternate_mobil_number=models.CharField(max_length=20)
    address=models.CharField(max_length=20)

    def __str__(self):
        return self.user_id

#FOR SHIPPING ADDRESS

class shippingadd(models.Model):   
    Addressline1=models.CharField(max_length=20)
    Addressline2=models.CharField(max_length=20)
    City=models.CharField(max_length=20)
    State=models.CharField(max_length=20)
    Zipcode=models.CharField(max_length=20)
    Country=models.CharField(max_length=20)
    
    def __str__(self):
        return self.Addressline1