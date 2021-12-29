# Generated by Django 3.2.10 on 2021-12-29 14:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    replaces = [('api', '0001_initial'), ('api', '0002_auto_20211229_1408'), ('api', '0003_alter_painting_inception_at')]

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Creator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Depiction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Movement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Painting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, null=True)),
                ('native_name', models.CharField(max_length=500, null=True)),
                ('wikidata_url', models.CharField(max_length=500, unique=True)),
                ('title', models.CharField(max_length=500, null=True)),
                ('picture_url', models.CharField(max_length=1000, null=True)),
                ('owned_by', models.CharField(max_length=500, null=True)),
                ('inception_at', models.CharField(max_length=10, null=True)),
                ('width', models.PositiveIntegerField(null=True)),
                ('height', models.PositiveIntegerField(null=True)),
                ('described_at', models.CharField(max_length=500, null=True)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('updated_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('creators', models.ManyToManyField(related_name='paintings', to='api.Creator')),
                ('depicts', models.ManyToManyField(related_name='paintings', to='api.Depiction')),
                ('genres', models.ManyToManyField(related_name='paintings', to='api.Genre')),
                ('locations', models.ManyToManyField(related_name='paintings', to='api.Location')),
                ('materials', models.ManyToManyField(related_name='paintings', to='api.Material')),
                ('movements', models.ManyToManyField(related_name='paintings', to='api.Movement')),
            ],
        ),
    ]
