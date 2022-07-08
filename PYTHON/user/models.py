import datetime
import uuid

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
# from community.models import Question
import community.models


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    favoriteQuestionID = models.ForeignKey(to='community.Question', on_delete=models.CASCADE, blank=True, null=True)
    date_created = models.DateTimeField(default=datetime.datetime.now)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return str(self.user.username)
