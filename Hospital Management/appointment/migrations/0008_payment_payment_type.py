# Generated by Django 3.0.5 on 2020-05-24 23:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0007_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_type',
            field=models.CharField(choices=[('I', 'Individual'), ('C', 'Consulting')], default='I', max_length=1),
        ),
    ]
