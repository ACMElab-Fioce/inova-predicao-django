# Generated by Django 5.0.4 on 2024-10-16 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassiFinDtNotific',
            fields=[
                ('id_dengue01', models.AutoField(primary_key=True, serialize=False)),
                ('dt_notific', models.DateField()),
                ('classi_fin', models.CharField(max_length=255)),
                ('quantidade', models.IntegerField()),
            ],
        ),
    ]