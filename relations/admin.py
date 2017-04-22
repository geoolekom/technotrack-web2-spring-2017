from django.contrib import admin
from relations.models import Friendship, FriendshipRequest

admin.site.register(FriendshipRequest)
admin.site.register(Friendship)
