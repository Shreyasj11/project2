# Generated by Django 4.1.5 on 2023-02-03 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='student_details',
            fields=[
                ('std_id', models.CharField(max_length=260, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=260)),
                ('std_age', models.PositiveIntegerField()),
                ('gender', models.CharField(max_length=100)),
                ('phone', models.PositiveSmallIntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
