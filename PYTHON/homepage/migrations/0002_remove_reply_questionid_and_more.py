# Generated by Django 4.0.4 on 2022-07-07 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reply',
            name='questionID',
        ),
        migrations.RemoveField(
            model_name='votequestion',
            name='questionID',
        ),
        migrations.RemoveField(
            model_name='votereply',
            name='replyID',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
        migrations.DeleteModel(
            name='Reply',
        ),
        migrations.DeleteModel(
            name='VoteQuestion',
        ),
        migrations.DeleteModel(
            name='VoteReply',
        ),
    ]