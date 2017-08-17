from django.db import models

# Create your models here.

class Order(models.Model):

    pd=(('frog1','Frog'),
        ('puzzle2','Puzzle'),
        ('Face3','Face'),
        ('Carpenter4','Carpenter'),
        ('Vehicles5','Vehicles'),
        ('Shapes6','Shapes'),
        ('Buttons7','Buttons')
       )


    Products = models.CharField(max_length=200,choices=pd,default="Frog",blank=False)
    quantity=models.PositiveIntegerField(default=1,blank=False)
    text =models.TextField(max_length=200,null=False,blank=False)
    Name=models.CharField(max_length=200,null=True,blank=False)
    Email=models.EmailField(blank=False,null=True)
    def  __str__(self):
         return self.Products
    

class Events(models.Model):
    Name =models.CharField(max_length=200,blank=False,null=True)
    Activity = models.TextField(max_length=200,blank=False,null=True)
    DateOfEvent =models.DateField(auto_now=False,null=True)
    def __str__(self):
        return self.Name


     


