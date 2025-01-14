# Generated by Django 5.0.6 on 2024-08-31 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobapps', '0002_jobfields_delete_jobfields1_delete_jobfields2'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobfields',
            name='country',
            field=models.CharField(choices=[('India', 'India'), ('United States', 'United States'), ('Canada', 'Canada'), ('Others', 'Others')], default='----', max_length=50),
        ),
        migrations.AddField(
            model_name='jobfields',
            name='pincode',
            field=models.BigIntegerField(blank=True, null=True, verbose_name=6),
        ),
        migrations.AddField(
            model_name='jobfields',
            name='state',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='jobfields',
            name='employment_type',
            field=models.CharField(choices=[('----', '----'), ('FT', 'Full-time'), ('PT', 'Part-time'), ('CT', 'Contract'), ('FL', 'Freelance'), ('IN', 'Internship')], default='----', max_length=4),
        ),
    ]
