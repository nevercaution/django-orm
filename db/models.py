from django.db import models

# Create your models here.


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'user'
