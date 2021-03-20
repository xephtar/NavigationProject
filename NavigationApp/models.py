from django.db import models


# Create your models here.

class TimeStampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, )
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Vehicle(TimeStampMixin):
    id = models.AutoField(primary_key=True)
    plate = models.CharField(max_length=10, blank=True, null=True, unique=True)


class NavigationRecord(TimeStampMixin):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.PROTECT)
    datetime = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
