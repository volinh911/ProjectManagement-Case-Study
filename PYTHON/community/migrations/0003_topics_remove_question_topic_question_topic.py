# Generated by Django 4.0.4 on 2022-07-07 07:56

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0002_alter_question_votepoints_alter_reply_votepoints'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topics',
            fields=[
                ('topic', models.CharField(choices=[('english', 'English'), ('mandarin', 'Mandarin'), ('german', 'German')], max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='question',
            name='topic',
        ),
        migrations.AddField(
            model_name='question',
            name='topic',
            field=models.ManyToManyField(to='community.topics'),
        ),
    ]