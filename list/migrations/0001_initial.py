# Generated by Django 3.2.6 on 2021-08-11 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Things',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('todo', models.CharField(max_length=200)),
                ('time_added', models.DateTimeField()),
                ('time_updated', models.DateTimeField(verbose_name='auto_now')),
            ],
        ),
    ]
