# Generated by Django 4.1.4 on 2023-10-13 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DM_Head', '0003_alter_employeeleave_end_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeleave',
            name='no_of_days',
            field=models.IntegerField(default=0),
        ),
    ]
