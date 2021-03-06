from userprofile.models import Users
from rest_framework.exceptions import APIException

class Authtication(object):
    def authenticate(self, request):
        if request.path == '/docs/':
            return (False, None)
        elif request.path == '/swagger':
                return (False, None)
        else:
            openid = request.META.get('HTTP_TOKEN')
            if openid:
                user = Users.objects.filter(openid__exact=str(openid)).first()
                return (True, user)
            else:
                raise APIException({"detail": "Please Add token to your request headers"})

    def authenticate_header(self, request):
        pass
