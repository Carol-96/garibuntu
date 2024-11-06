# Generated by Django 4.2.16 on 2024-11-06 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_initial'),
        ('sponsors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sponsor',
            name='company_name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='contact_person',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='sponsor',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='Sponsorship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sponsored_at', models.DateTimeField(auto_now_add=True)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.event')),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sponsors.sponsor')),
            ],
        ),
    ]
