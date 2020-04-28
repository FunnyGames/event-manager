# Generated by Django 3.0.5 on 2020-04-28 09:48

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('event', '0009_auto_20200417_0927'),
    ]

    operations = [
        migrations.CreateModel(
            name='RateEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('EventId', models.IntegerField(default=0)),
                ('rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)])),
                ('create_date', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='rateevent',
            constraint=models.CheckConstraint(check=models.Q(rate__range=(1, 5)), name='valid_rate'),
        ),
        migrations.AddConstraint(
            model_name='rateevent',
            constraint=models.UniqueConstraint(fields=('user', 'EventId'), name='rating_once'),
        ),
    ]
