# Generated by Django 4.1.1 on 2022-10-02 02:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.CharField(max_length=250)),
                ('aka', models.CharField(blank=True, max_length=100)),
                ('bio', models.TextField(max_length=500)),
                ('see_also', models.CharField(blank=True, max_length=200)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
