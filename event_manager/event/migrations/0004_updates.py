# Generated by Django 3.0.4 on 2020-04-16 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0003_auto_20200416_1635'),
    ]

    operations = [
        migrations.CreateModel(
            name='Updates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventId', models.IntegerField(default=0)),
                ('cancelled', models.BooleanField(default=False)),
            ],
        ),
    ]
