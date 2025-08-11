from django.db import models

class CategoryModel (models.Model):
    name_category = models.CharField(max_length=200,null=False)
    level_category = models.IntegerField(null=False)

    def __str__(self):
        return self.name_category