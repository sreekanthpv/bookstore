from django.db import models
from datetime import timedelta,date

class Book(models.Model):
    book_name=models.CharField(max_length=100,unique=True,blank=True)
    author=models.CharField(max_length=100)
    price=models.IntegerField()
    copies=models.PositiveIntegerField()
    image=models.ImageField(upload_to="image",null=True)
    # catagory=models.CharField(max_length=100)

    def __str__(self):
        return self.book_name

# book=Book(book_name="randamoozham",author="mt",price=200,copies=50)
# book.save()
#books=Book.objects.all()

#orm for fetching a specific record
   # reference=modelname.objects.get(fieldname=value)
   # book=Book.objects.get(id=1)

#orm query for updating specific record
   # book=Book.objects.get(id=1)
   # book.price=250
   #book.save()


class Order(models.Model):

    product=models.ForeignKey(Book,on_delete=models.CASCADE)
    user=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    options=(
        ("delivered","delivered"),("intransit","intransit"),("ordered","ordered"),("cancelled","cancelled")
    )
    status=models.CharField(max_length=20,choices=options,default="ordered")
    phone_number=models.CharField(max_length=20)
    edd=date.today()+timedelta(days=3)
    expected_delivery_date=models.DateField(default=edd,null=True)


