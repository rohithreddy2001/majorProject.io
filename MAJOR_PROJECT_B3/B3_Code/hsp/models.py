from django.db import models



class patientdatamodel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    mobileno = models.CharField(max_length=50, default="", editable=True)
    gender = models.CharField(max_length=50, default="", editable=True)
    weight= models.CharField(max_length=40, default="", editable=True)
    age= models.CharField(max_length=40, default="", editable=True)
    symptomps= models.CharField(max_length=40, default="", editable=True)
    doctor=models.CharField(max_length=40, default="", editable=True)
    file = models.FileField(upload_to='files/pdfs/')


    def __str__(self):
        return self.email

    class Meta:
        db_table = 'patientdata'



