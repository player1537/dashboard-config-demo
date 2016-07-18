from django.db import models

# Create your models here.

class Facility(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return "Facility(name={self.name})".format(self=self)

class Instrument(models.Model):
    name = models.CharField(max_length=32)
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, related_name='instruments')

    def __str__(self):
        return "Instrument(name={self.name}, facility={self.facility})".format(
            self=self,
        )

class Configuration(models.Model):
    name = models.CharField(max_length=32)
    instrument = models.ForeignKey(Instrument, on_delete=models.CASCADE)

    def __str__(self):
        return "Configuration(name={self.name}, instrument={self.instrument})".format(
            self=self,
        )

class Entry(models.Model):
    name = models.CharField(max_length=32)
    key = models.CharField(max_length=32)
    value = models.CharField(max_length=32)
    advanced = models.BooleanField()

    def __str__(self):
        return "Entry(name={self.name}, key={self.key}, value={self.value}, advanced={self.advanced})".format(
            self=self,
        )
