from django.db import models
from django.contrib.auth.models import AbstractUser, Group

class Department(models.Model):
    name = models.CharField(max_length=100)
    diagnostics = models.TextField()
    location = models.CharField(max_length=255)
    specialization = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class User(AbstractUser):
    is_doctor = models.BooleanField(default=False)
    is_patient = models.BooleanField(default=False)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)

    def assign_to_department(self, department):
        self.department = department
        self.save()

class PatientRecord(models.Model):
    record_id = models.AutoField(primary_key=True)
    patient = models.ForeignKey(User, related_name='patient_records', on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    diagnostics = models.TextField()
    observations = models.TextField()
    treatments = models.TextField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    misc = models.TextField(blank=True, null=True)