# Generated by Django 4.0.3 on 2022-04-21 10:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='E nevojshme', max_length=255, unique=True, verbose_name='Emri')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Qyteti',
                'verbose_name_plural': 'Qytetet',
            },
        ),
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Vendos titullin e njoftimit', max_length=500, verbose_name='Titulli')),
                ('description', models.CharField(help_text='Vendos pershkrimin', max_length=1000, verbose_name='Pershkrimi')),
                ('price', models.IntegerField()),
                ('area', models.ImageField(upload_to='')),
                ('views', models.IntegerField(default=0)),
                ('documents', models.CharField(help_text='Dokumentat', max_length=255, verbose_name='Dokumentacioni')),
                ('status', models.BooleanField(default=True)),
                ('activity', models.CharField(choices=[('Sale', 'Shitje'), ('Rent', 'Qera')], max_length=20)),
                ('property_type', models.CharField(choices=[('Apartament', 'Apartament'), ('Vila', 'Vila'), ('Store', 'Dyqan'), ('Land', 'Truall'), ('Garage', 'Garazhd')], max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_creator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Prona',
                'verbose_name_plural': 'Pronat',
            },
        ),
        migrations.CreateModel(
            name='Villa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('floors', models.IntegerField(default=1)),
                ('room_num', models.IntegerField(default=1)),
                ('bath_num', models.IntegerField(default=1)),
                ('balcony_num', models.IntegerField(default=0)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.property', unique=True)),
            ],
            options={
                'verbose_name': 'Vila',
                'verbose_name_plural': 'Vilat',
            },
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('floor', models.IntegerField(default=0)),
                ('bath_num', models.IntegerField(default=1)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.property', unique=True)),
            ],
            options={
                'verbose_name': 'Dyqan',
                'verbose_name_plural': 'Dyqanet',
            },
        ),
        migrations.CreateModel(
            name='PropertyImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default='images/default.png', help_text='Upload a property image', upload_to='images/', verbose_name='image')),
                ('alt_text', models.CharField(blank=True, help_text='Please add alturnative text', max_length=255, null=True, verbose_name='Alturnative text')),
                ('is_feature', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='property_image', to='pronat.property')),
            ],
            options={
                'verbose_name': 'Property Image',
                'verbose_name_plural': 'Property Images',
            },
        ),
        migrations.CreateModel(
            name='Land',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.property', unique=True)),
            ],
            options={
                'verbose_name': 'Toke',
                'verbose_name_plural': 'Tokat',
            },
        ),
        migrations.CreateModel(
            name='Garage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('floor', models.IntegerField()),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.property', unique=True)),
            ],
            options={
                'verbose_name': 'Garazhd',
                'verbose_name_plural': 'Garazhdet',
            },
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='E nevojshme', max_length=255, unique=True, verbose_name='Emri')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('city_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.city')),
            ],
            options={
                'verbose_name': 'Zona',
                'verbose_name_plural': 'Zonat',
            },
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('floor', models.IntegerField(default=0)),
                ('room_num', models.IntegerField(default=0)),
                ('bath_num', models.IntegerField(default=0)),
                ('balcony_num', models.IntegerField(default=0)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.property', unique=True)),
            ],
            options={
                'verbose_name': 'Apartament',
                'verbose_name_plural': 'Apartamentet',
            },
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address_line', models.CharField(help_text='E nevojeshme', max_length=255, verbose_name='Adresa')),
                ('district_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pronat.district')),
            ],
            options={
                'verbose_name': 'Adresa',
            },
        ),
    ]