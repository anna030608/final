# Generated by Django 3.1.3 on 2023-05-22 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
