# Generated by Django 2.2.4 on 2019-08-12 04:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('administrador', '0001_initial'),
        ('tratamiento', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tratamiento',
            name='persona',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='administrador.Persona'),
        ),
    ]