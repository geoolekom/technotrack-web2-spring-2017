from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from api.views import ChatDetail, ChatList, UserDetail, UserList, MessageDetail, MessageList
#from api.views import PostDetail, PostList

urlpatterns = [
	url(r'users/(?P<pk>\d+)', UserDetail.as_view(), name='user-detail'),
	url(r'users/$', UserList.as_view(), name='user-list'),
	url(r'chats/(?P<pk>\d+)', ChatDetail.as_view(), name='chat-detail'),
	url(r'chats/$', ChatList.as_view(), name='chat-list'),
	url(r'messages/(?P<pk>\d+)', MessageDetail.as_view(), name='message-detail'),
	url(r'messages/$', MessageList.as_view(), name='message-list'),
#	url(r'posts/(?P<pk>\d+)', PostDetail.as_view(), name='post-detail'),
#	url(r'posts/$', PostList.as_view(), name='post-list'),
#	url(r'comments/(?P<pk>\d+)', CommentDetail.as_view(), name='comment-detail'),
#	url(r'comments/$', CommentList.as_view(), name='comment-list'),
]

urlpatterns = format_suffix_patterns(urlpatterns)