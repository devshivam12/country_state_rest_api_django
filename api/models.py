from django.db import models
# Create your models here.



#This is a Country Model
class Country(models.Model):
    Country_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    status=models.BooleanField(default=True)


    def __str__(self):
        return self.name


class State(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)

    Country = models.ForeignKey(Country, on_delete=models.CASCADE)
    # Country_id = models.ForeignKey(Country,on_delete=models.CASCADE)

    # def __str__(self):
    #     return self.name
class Customer(models.Model):
    name=models.CharField(max_length=50)
    




