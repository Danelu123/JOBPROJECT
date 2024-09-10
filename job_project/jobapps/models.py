# jobapps models file

from django.db import models

class JobFields(models.Model):
    EMPLOYMENT_TYPES = [
        ('----', '----'),
        ('FT', 'Full-time'),
        ('PT', 'Part-time'),
        ('CT', 'Contract'),
        ('FL', 'Freelance'),
        ('IN', 'Internship'),
    ]
    title = models.CharField(max_length=255)
    company = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    state = models.CharField(max_length=255,null=True, blank=True)
    pincode = models.BigIntegerField(6,null=True, blank=True)
    country = models.CharField(max_length=50,choices=[('India', 'India'), ('United States', 'United States'),
                            ('Canada', 'Canada'),('Others', 'Others')],default='----')
    experience_level = models.CharField(max_length=50,choices=[('Entry-Level', 'Entry-Level'), ('Mid-Level', 'Mid-Level'),
                            ('Senior-Level', 'Senior-Level')])
    employment_type = models.CharField(max_length=4, choices=EMPLOYMENT_TYPES,default='----')
    description = models.TextField()
    requirements = models.TextField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    application_deadline = models.DateField(null=True, blank=True)
    posted_date = models.DateField(null=True, blank=True)
    def __str__(self):
        return self.title



