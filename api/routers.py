from rest_framework import routers

import api.views

router = routers.DefaultRouter()

router.register('users', api.views.UserViewSet)
router.register('chats', api.views.ChatViewSet)
router.register('messages', api.views.MessageViewSet)
router.register('posts', api.views.PostViewSet)
router.register('comments', api.views.CommentViewSet)
router.register('achievements', api.views.AchievementViewSet)
router.register('notifications', api.views.NotificationViewSet)
router.register('likes', api.views.LikeViewSet)
router.register('friends', api.views.FriendshipViewSet)
router.register('requests', api.views.FriendshipRequestViewSet)
