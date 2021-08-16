# Generated by Django 3.2.6 on 2021-08-13 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ovrapp', '0005_auto_20210813_1643'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='Reporting_Department_Section_athor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Reporting_Department_Section_athor', to='ovrapp.section_list'),
        ),
        migrations.AddField(
            model_name='order',
            name='Responding_Department_Section',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Responding_Department_Section', to='ovrapp.section_list'),
        ),
    ]