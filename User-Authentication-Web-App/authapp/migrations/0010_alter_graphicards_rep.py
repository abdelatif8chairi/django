# Generated by Django 4.0.2 on 2022-02-05 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0009_alter_graphicards_rep'),
    ]

    operations = [
        migrations.AlterField(
            model_name='graphicards',
            name='Rep',
            field=models.FileField(upload_to='static/images'),
        ),
    ]
