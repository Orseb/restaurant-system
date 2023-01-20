from django.db import models

# Create your models here.
class Booking(models.Model):
    Name = models.CharField(max_length=255)
    No_of_guests = models.IntegerField()
    BookingDate = models.DateTimeField()

class Menu(models.Model):
    Title = models.CharField(max_length=255)
    Price = models.DecimalField(decimal_places=2, max_digits=6)
    Inventory = models.SmallIntegerField()

    def __str__(self):
        return f'{self.Title} : {str(self.Price)}'

    def get_item(self):
        return f'{self.Title} : {str(self.Price)}'
