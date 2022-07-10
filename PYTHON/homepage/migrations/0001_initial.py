# Generated by Django 4.0.4 on 2022-07-07 07:08

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField(max_length=2000)),
                ('topic', models.CharField(choices=[('english', 'English'), ('mandarin', 'Mandarin'), ('german', 'German')], max_length=200)),
                ('votePoints', models.IntegerField(blank=True, default=0, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Reply',
            fields=[
                ('votePoints', models.IntegerField(blank=True, default=0, null=True)),
                ('content', models.TextField(max_length=2000)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.question')),
            ],
        ),
        migrations.CreateModel(
            name='VoteReply',
            fields=[
                ('type', models.CharField(choices=[('up', 'Up'), ('down', 'Down')], max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('replyID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.reply')),
            ],
        ),
        migrations.CreateModel(
            name='VoteQuestion',
            fields=[
                ('type', models.CharField(choices=[('up', 'Up'), ('down', 'Down')], max_length=200)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.question')),
            ],
        ),
    ]
