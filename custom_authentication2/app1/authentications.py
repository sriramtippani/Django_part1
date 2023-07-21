from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.models import User

# class C1(BaseAuthentication):
#     def authenticate(self, request):
#         username = request.GET.get('username')
#         if username is None:
#             return None
#         else:
#             try:
#                 user = User.objects.get(username=username)
#             except User.DoesNotExist:
#                 raise AuthenticationFailed('No such type of user')
#             return (user, None)


class M1(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        key = request.GET.get('key')
        if username is None or key is None:
            return None
        else:
            c1 = len(key) == 7
            c2 = key[0] == username[-1].lower()
            c3 = key[2] == 'Z'
            c4 = key[4] == username[0]
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                raise AuthenticationFailed('your provided user name is invalid, please provide valid username')

            if c1 and c2 and c3 and c4:
                return user, None
            else:
                raise AuthenticationFailed('your provided key is invalid, please provide valid key to access end point')

