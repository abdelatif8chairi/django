# Generated by Django 4.0.2 on 2022-02-05 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_student_delete_graphicards'),
    ]

    operations = [
        migrations.CreateModel(
            name='GraphiCards',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('Rep', models.TextField()),
                ('Quantity', models.FloatField()),
                ('Price', models.FloatField()),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]