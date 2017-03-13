from rest_framework import routers

import api.views

router = routers.DefaultRouter()

router.register('users', api.views.UserViewSet)
router.register('chats', api.views.ChatViewSet)
router.register('messages', api.views.MessageViewSet)
router.register('comments', api.views.CommentViewSet)