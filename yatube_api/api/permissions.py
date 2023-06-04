from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    """Редактирование объекта, только владельцам объекта."""
    def has_object_permission(self, request, view, obj):
        """Чтение разрешено для любого запроса, GET, HEAD или OPTIONS."""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user
