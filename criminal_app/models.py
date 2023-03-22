from django.db import models


class Criminal(models.Model):
    name = models.TextField(blank=True)
    criminal_number = models.TextField(blank=True)
    nickname = models.TextField(blank=True)
    address = models.TextField(blank=True)
    date_of_crime = models.TextField(blank=True)
    arrest_date = models.TextField(blank=True)
    occupation = models.TextField(blank=True)
    crime_type = models.TextField(blank=True)
    age = models.TextField(blank=True)
    fathers_name = models.TextField(blank=True)
    gender = models.TextField(blank=True)
    wanted = models.TextField(blank=True)
    criminal_image = models.ImageField(blank=True, null=True, upload_to='images')

    def __str__(self):
        return self.name + ' ' + self.criminal_number
