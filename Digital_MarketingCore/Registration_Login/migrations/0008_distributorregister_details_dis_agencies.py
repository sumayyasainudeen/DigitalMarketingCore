# Generated by Django 4.2.5 on 2023-10-05 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registration_Login', '0007_distributorregister_details'),
    ]

    operations = [
        migrations.AddField(
            model_name='distributorregister_details',
            name='dis_agencies',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
    ]
