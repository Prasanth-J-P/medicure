# Generated by Django 4.2.7 on 2024-02-02 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storeroom', '0003_alter_medicinedetails_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicinedetails',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]
