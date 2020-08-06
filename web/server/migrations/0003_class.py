# Generated by Django 3.1 on 2020-08-06 18:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20200806_1509'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(max_length=20)),
                ('start', models.CharField(max_length=5)),
                ('end', models.CharField(max_length=5)),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='classes', to='server.teacher')),
            ],
        ),
    ]
