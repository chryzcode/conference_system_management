# Generated by Django 3.2.4 on 2021-11-17 01:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conference_app', '0002_alter_talk_conference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='talk',
            name='conference',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='conference_app.conference'),
        ),
    ]