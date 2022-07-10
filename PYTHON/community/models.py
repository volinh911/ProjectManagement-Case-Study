import datetime
import uuid

from django.db import models

from user.models import Profile

VOTE_TYPE = (
    ('up', 'Up'),
    ('down', 'Down'),
)

QUESTION_TOPIC = (
    ('English', 'English'),
    ('Mandarin', 'Mandarin'),
    ('German', 'German'),
)


# Create your models here.
class Question(models.Model):
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    topic = models.CharField(max_length=200, choices=QUESTION_TOPIC, null=False)
    votePoints = models.IntegerField(default=0, null=True, blank=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.title


class Reply(models.Model):
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
    votePoints = models.IntegerField(default=0, null=True, blank=True)
    content = models.TextField(max_length=2000)
    date_created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.content


class VoteQuestion(models.Model):
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    type = models.CharField(max_length=200, choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.type


class VoteReply(models.Model):
    replyID = models.ForeignKey(Reply, on_delete=models.CASCADE)
    owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)

    type = models.CharField(max_length=200, choices=VOTE_TYPE)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.type
