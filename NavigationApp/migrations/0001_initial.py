# Generated by Django 3.1.7 on 2021-03-19 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('plate', models.CharField(blank=True, max_length=10, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='NavigationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('vehicle', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='NavigationApp.vehicle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
