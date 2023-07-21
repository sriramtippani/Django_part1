from rest_framework.permissions import BasePermission, SAFE_METHODS
class IsReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            return False

class IsGETOrPatch(BasePermission):
    def has_permission(self, request, view):
        allowed_methods = ['GET', 'PATCH', 'DELETE']
        if request.method in allowed_methods:
            return True
        else:
            return False

class OurOwnPermissions(BasePermission):
    def has_permission(self, request, view):
        username = request.user.username
        if username != '' and len(username) % 2 == 0 and request.method in SAFE_METHODS:
            return True
        elif username.lower() == 'sriram':
            return True
        else:
            return False