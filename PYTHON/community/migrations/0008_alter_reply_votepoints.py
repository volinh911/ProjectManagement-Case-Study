# Generated by Django 4.0.4 on 2022-07-07 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0007_alter_question_votepoints'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reply',
            name='votePoints',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
