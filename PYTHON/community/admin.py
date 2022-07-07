from django.contrib import admin

from .models import Question, Reply, VoteQuestion, VoteReply

# Register your models here.
admin.site.register(Question)
admin.site.register(Reply)
admin.site.register(VoteQuestion)
admin.site.register(VoteReply)
