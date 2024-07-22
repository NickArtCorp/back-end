from django.db import models

class Menu(models.Model):
    menuID = models.IntegerField()
    title = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    inventory = models.IntegerField()

    def __str__(self):
        return f'{self.title} : {str(self.price)}'

    
    
class Booking(models.Model):
    customer_id = models.IntegerField()
    customer_name = models.CharField(max_length=255)
    BookingDate = models.DateField()
    number_of_guests = models.PositiveIntegerField()
   

    def __str__(self):
        return f"{self.customer_name} - {self.BookingDate}"
    

    

