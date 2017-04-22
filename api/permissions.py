from rest_framework import permissions


class IsAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.author_id == request.user.id


class IsConsumer(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.consumer_id == request.user.id


class IsChatParticipantOrAuthor(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS and request.user in obj.participants.all():
            return True
        else:
            return obj.author_id == request.user.id


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.author_id == request.user.id


class IsAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_superuser


class IsAdminOrCanRegister(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'PUT':
            return request.user == obj

    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        elif request.method == 'POST':
            return not (request.user and request.user.is_authenticated)


class IsPersonOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.is_superuser or request.user.id == obj.person_id


class IsAuthorOrTargetOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return request.user.id == obj.author_id or request.user.id == obj.target_id
