# Generated by Django 4.0.6 on 2022-07-20 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('persona', '0003_habilidad_alter_empleado_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleado',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='habilidades',
            field=models.ManyToManyField(to='persona.habilidad'),
        ),
    ]