from django.db import models

# Create your models here.
class Reminder(models.Model):
    reminder_id = models.AutoField(primary_key=True)
    item_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=20)
    notes = models.TextField()

    def __str__(self):
        return self.item_name