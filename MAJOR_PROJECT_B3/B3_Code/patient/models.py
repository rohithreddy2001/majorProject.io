from django.db import models


class patientModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    passwd = models.CharField(max_length=40)
    cwpasswd = models.CharField(max_length=40)
    mobileno = models.CharField(max_length=50, default="", editable=True)
    status = models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='patientregister'

class patienttreatmentModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    symptomps = models.CharField(max_length=40, default="", editable=True)
    treatment=models.CharField(max_length=40, default="", editable=True)

    def  __str__(self):
        return self.email

    class Meta:
        db_table='patienttreatment'









