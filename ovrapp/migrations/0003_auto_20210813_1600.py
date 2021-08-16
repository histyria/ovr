# Generated by Django 3.2.6 on 2021-08-13 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ovrapp', '0002_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Informed',
            field=models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='RLikelihood_Category',
            field=models.CharField(choices=[('Unlikely', 'Unlikely'), ('Possible', 'Possible'), ('Likely', 'Likely'), ('Almost Certain', 'Almost Certain')], max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='Type_of_Injury',
            field=models.CharField(choices=[('Physical', 'Physical'), ('Psychological', 'Psychological')], max_length=200, null=True),
        ),
    ]
