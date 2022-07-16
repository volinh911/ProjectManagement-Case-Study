import datetime

from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from vote.models import VoteModel
from pytz import timezone
from datetime import datetime

VOTE_TYPE = (
    ('up', 'Up'),
    ('down', 'Down'),
)

QUESTION_TOPIC = (
    ('English', 'English'),
    ('Mandarin', 'Mandarin'),
    ('German', 'German'),
)
tz = timezone('Asia/Ho_Chi_Minh')

# Create your models here.
class Question(VoteModel, models.Model):
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    title = models.CharField(max_length=200)
    content = models.TextField(max_length=2000)
    topic = models.CharField(max_length=200, choices=QUESTION_TOPIC, null=False)
    date_created = models.DateTimeField(default=datetime.now(tz))
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.title


class Reply(VoteModel, models.Model):
    questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
    owner = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    content = models.TextField(max_length=2000)
    date_created = models.DateTimeField(default=datetime.now(tz))
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.content

# class VoteQuestion(models.Model):
#     questionID = models.ForeignKey(Question, on_delete=models.CASCADE)
#     owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
#
#     type = models.CharField(max_length=200, choices=VOTE_TYPE)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#
#     def __str__(self):
#         return self.type
#
#
# class VoteReply(models.Model):
#     replyID = models.ForeignKey(Reply, on_delete=models.CASCADE)
#     owner = models.ForeignKey(Profile, null=True, blank=True, on_delete=models.SET_NULL)
#
#     type = models.CharField(max_length=200, choices=VOTE_TYPE)
#     id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
#
#     def __str__(self):
#         return self.type
