# Generated by Django 5.0.6 on 2024-08-25 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.EmailField(max_length=254)),
                ('Phone_Number', models.BigIntegerField(verbose_name=10)),
                ('Location', models.CharField(max_length=100)),
                ('Current_Job_Title', models.CharField(max_length=100)),
                ('Current_Employer', models.CharField(max_length=100)),
                ('Work_Experience', models.CharField(max_length=100)),
                ('Skills', models.CharField(max_length=500)),
                ('Highest_Degree_Achieved', models.CharField(max_length=100)),
                ('Institutions_Attended', models.CharField(max_length=100)),
                ('Field_of_Study', models.CharField(max_length=100)),
                ('Graduation_Year', models.IntegerField()),
                ('Certification_Name', models.CharField(max_length=100)),
                ('Issuing_Organization', models.CharField(max_length=100)),
                ('Project_links', models.CharField(max_length=100)),
                ('Languages_Spoken', models.CharField(max_length=100)),
                ('Availability', models.CharField(max_length=100)),
                ('Preferred_Job_Location', models.CharField(max_length=100)),
                ('Resume', models.FileField(blank=True, null=True, upload_to='resumes/')),
                ('Profile_Image', models.ImageField(blank=True, null=True, upload_to='profile_images/')),
            ],
        ),
    ]
