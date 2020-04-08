from django.db import models

class Covid(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(default=0)
    breath = models.BooleanField(default=False)
    fever = models.BooleanField(default=False)
    cough = models.BooleanField(default=False)
    chills = models.BooleanField(default=False)
    sudden_confusion = models.BooleanField(default=False)
    digestive = models.BooleanField(default=False)
    pink_eye = models.BooleanField(default=False)
    loss_taste = models.BooleanField(default=False)
    fatigue = models.BooleanField(default=False)
    congestion = models.BooleanField(default=False)

    def __str__(self):
        return self.name