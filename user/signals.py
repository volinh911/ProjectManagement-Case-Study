# from django.contrib.auth.models import User
# from django.db.models.signals import post_save, post_delete
#
# from .models import Profile
#
#
# def createUser(sender, instance, created, **kwargs):
#     if created:
#         user = instance
#         profile = Profile.objects.create(
#             user=user
#         )
#
#
# def deleteProfile(sender, instance, created, **kwargs):
#     user = instance.user
#     user.delete()
#
#
# post_save.connect(createUser, sender=User)
# post_delete.connect(createUser, sender=Profile)
