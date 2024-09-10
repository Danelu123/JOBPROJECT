# # fieldsapp models file

from django.db import models

class Profile(models.Model):
    Name = models.CharField(max_length=100,null=True, blank=True)
    Email = models.EmailField(null=True, blank=True)
    Phone_Number = models.BigIntegerField(10,null=True, blank=True)
    Location = models.CharField(max_length=100)
    State = models.CharField(max_length=100,null=True, blank=True)
    Country = models.CharField(max_length=50, choices=[('----', '----'),('India', 'India'), ('United States', 'United States'),
                                                       ('Canada', 'Canada'), ('Others', 'Others')],default='----')
    Current_Job_Title = models.CharField(max_length=100)
    Current_Employer = models.CharField(max_length=100)
    Work_Experience = models.CharField(max_length=100)
    Skills = models.CharField(max_length=500)
    Highest_Degree_Achieved = models.CharField(max_length=100)
    Institutions_Attended = models.CharField(max_length=100)
    Field_of_Study = models.CharField(max_length=100)
    Graduation_Year = models.IntegerField()
    Certification_Name = models.CharField(max_length=100)
    Issuing_Organization = models.CharField(max_length=100)
    Project_links = models.CharField(max_length=100)
    Languages_Spoken = models.CharField(max_length=100)
    Availability = models.CharField(max_length=100)
    Preferred_Job_Location = models.CharField(max_length=100)
    Resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    Profile_Image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    def __str__(self):
        return self.Name
