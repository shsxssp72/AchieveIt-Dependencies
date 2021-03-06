# Generated by Django 3.0.4 on 2020-03-05 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AchieveItDependencies', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customers',
            fields=[
                ('customer_id', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('referred_coordinator_id', models.BigIntegerField()),
                ('corporation_name', models.CharField(max_length=255)),
                ('customer_level', models.CharField(max_length=10)),
                ('customer_email', models.CharField(max_length=255)),
                ('customer_telephone', models.CharField(max_length=15)),
                ('customer_address', models.CharField(max_length=255)),
            ],
        ),
    ]
