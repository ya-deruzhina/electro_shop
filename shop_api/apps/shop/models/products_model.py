from django.db import models


class ProductModel (models.Model):
    name = models.CharField(max_length=25,null=False)
    model = models.CharField(max_length=200,null=False)
    launch_date = models.DateTimeField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    