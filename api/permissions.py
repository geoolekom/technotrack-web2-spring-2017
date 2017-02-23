from rest_framework import permissions


class IsAuthor(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		return obj.author_id == request.user.id


class IsChatParticipantOrAuthor(permissions.BasePermission):

	def has_object_permission(self, request, view, obj):
		if request.method in permissions.SAFE_METHODS and request.user in obj.participants.all():
			return True
		else:
			return obj.author_id == request.user.id
