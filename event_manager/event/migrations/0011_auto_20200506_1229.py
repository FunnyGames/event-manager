# Generated by Django 3.0.4 on 2020-05-06 12:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0010_auto_20200428_1248'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventId', models.IntegerField(default=0)),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='myevent',
            constraint=models.UniqueConstraint(fields=('user', 'EventId'), name='events_once'),
        ),
    ]