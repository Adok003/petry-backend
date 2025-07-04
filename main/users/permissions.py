from rest_framework.permissions import BasePermission

class IsSuperAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'superadmin'

class IsExecutor(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role and request.user.role.name == 'executor'

class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        return (
            request.user.is_authenticated and
            request.user.role and
            request.user.role.name == 'accountant'
        )