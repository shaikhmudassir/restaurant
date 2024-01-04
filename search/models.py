from django.db import models

class Restaurant(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    lat_long = models.CharField(max_length=200)
    other_details = models.JSONField()

    def __str__(self):
        return self.name + " (" + self.location + ")"
    

class Dishes(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    item = models.CharField(max_length=200)
    price = models.CharField(max_length=50)

    def __str__(self):
        return self.item + " " + self.restaurant.name