# Generated by Django 3.2.9 on 2022-04-18 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('neighborapp', '0002_neighborhood_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='neighborhood',
            name='occupants_count',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='biz_name',
            field=models.TextField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='business',
            name='email_address',
            field=models.EmailField(max_length=100, null=True),
        ),
    ]
