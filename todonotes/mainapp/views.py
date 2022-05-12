from yaml import serialize
from rest_fraemwork.viewsets import ModelViewSet
from .models import User
from .serializers import UserModelSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer
    
