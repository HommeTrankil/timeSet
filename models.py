from django.db import models
# Create your models here.

class timePick(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(blank=True, null=True )

    def __str__(self):
        return self.title


class timeTest(models.Model):
    title = models.CharField(max_length=200)
    timeStart = models.DateTimeField(blank=True, null=True )
    timeEnd = models.DateTimeField(blank=True, null=True )
    url = models.CharField(max_length=600)

    select = (
        ("default", "default"),

	    ("success", "success"),
        ("info", "info"),
        ("important", "important"))

    className = models.CharField(max_length=20 , default='default', choices=select)

    def __str__(self):
        return self.title


class sugarTest(models.Model):

    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=200)
    email = models.CharField(max_length=200)


    select = (
        ("default", "default"),
	    ("success", "success"),
        ("info", "info"),
        ("important", "important"))

    service = models.CharField(max_length=20 , default='default', choices=select)

    holiday_date = models.DateField(blank=True, null=True)
    contact_time = models.TimeField(blank=True, null=True)

    comment = models.TextField()


    def __str__(self):
        return self.name
