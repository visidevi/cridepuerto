# Generated by Django 3.2.7 on 2021-09-14 23:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('comments', models.TextField(blank=True)),
                ('rating', models.IntegerField(default=1)),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Ride',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Date time on which the object was created.', verbose_name='created at')),
                ('modified', models.DateTimeField(auto_now=True, help_text='Date time on which the object was last modified.', verbose_name='modified at')),
                ('available_seats', models.PositiveSmallIntegerField(default=1)),
                ('comments', models.TextField(blank=True)),
                ('departure_location', models.CharField(max_length=255)),
                ('departure_date', models.DateTimeField()),
                ('arrival_location', models.CharField(max_length=255)),
                ('arrival_date', models.DateTimeField()),
                ('rating', models.FloatField(null=True)),
                ('is_active', models.BooleanField(default=True, help_text='Used for disabling the ride or marking it as finished.', verbose_name='active status')),
            ],
            options={
                'ordering': ['-created', '-modified'],
                'get_latest_by': 'created',
                'abstract': False,
            },
        ),
    ]
