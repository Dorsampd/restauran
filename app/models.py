from django.db import models

# Create your models here.
class foods(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField()
    img=models.ImageField(upload_to="photo",null=True)
    price=models.IntegerField

    def __str__(self) -> str:
        return super().__str__() 