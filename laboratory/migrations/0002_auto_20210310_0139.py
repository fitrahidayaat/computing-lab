# Generated by Django 3.1.7 on 2021-03-10 01:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laboratory', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='description',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='generation',
            field=models.CharField(blank=True, max_length=3, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='linkedin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/members'),
        ),
        migrations.AlterField(
            model_name='member',
            name='student_year',
            field=models.CharField(blank=True, max_length=4, null=True),
        ),
    ]
