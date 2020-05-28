from django.db import models
from datetime import datetime
class Payroll(models.Model):
    date = models.CharField(max_length=20, null=False)
    hours_worked = models.FloatField()
    employee_id = models.IntegerField(null=False)
    job_group = models.CharField(max_length=1)
    def __str__(self):
        return self.date