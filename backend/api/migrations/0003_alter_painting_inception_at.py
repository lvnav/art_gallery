# Generated by Django 3.2.10 on 2021-12-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20211229_1408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='painting',
            name='inception_at',
            field=models.CharField(max_length=10, null=True),
        ),
    ]