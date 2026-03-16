from rest_framework.permissions import BasePermission, SAFE_METHODS, DjangoModelPermissions


# https://www.django-rest-framework.org/api-guide/permissions/
class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


# Work with Django Group Permissions
class FullDjangoModelPermissions(DjangoModelPermissions):
    def __init__(self):
        self.perms_map['GET'] = ['%(app_label)s.view_%(model_name)s']