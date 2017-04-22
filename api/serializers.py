from rest_framework import serializers

from accounts.models import User
from chats.models import Chat, Message
from comments.models import Comment
from notifications.models import Notification
from achievements.models import Achievement
from likes.models import Like
from relations.models import Friendship, FriendshipRequest
from feed.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name',)


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'password',)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'author', 'chat', 'pub_time', 'upd_time', 'content',)


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat
        fields = ('id', 'author', 'title', 'participants',)


class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields = ('id', 'consumer', 'content',)


class PostSerializer(serializers.ModelSerializer):
    like_count = serializers.ReadOnlyField(source='likes.count')
    author = serializers.ReadOnlyField(source='author.id')

    class Meta:
        model = Post
        fields = ('id', 'author', 'title', 'content', 'like_count',)


class CommentSerializer(serializers.ModelSerializer):
    like_count = serializers.ReadOnlyField(source='likes.count')

    class Meta:
        model = Comment
        fields = ('id', 'author', 'content', 'like_count', 'target_content_type', 'target_id',)


class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = ('id', 'author', 'title', 'content',)


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('id', 'author', 'target_content_type', 'target_id',)


class FriendshipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Friendship
        fields = ('id', 'person', 'friend',)


class FriendshipRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = FriendshipRequest
        fields = ('id', 'author', 'target', 'accepted')
