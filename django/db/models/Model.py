from django.db import models


class Person(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField()

class consult(models.Model):
    id = models.BigAutoField(primary_key=True)
    date = models.DateField()
    hours = models.TimeField()
    idPerson = models.BigAutoField(models.ForeignKey(Person, verbose_name=_("Person"), on_delete=models.CASCADE))
    
class dr(models.Model):
    id = models.BigAutoField(primary_key=True)
    idPerson = models.BigIntegerField(models.ForeignKey(Person, verbose_name=_("Person"), on_delete=models.CASCADE)) #foreing key Person
    status = models.enums(["on","off"])
    