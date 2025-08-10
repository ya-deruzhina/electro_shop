from rest_framework import generics, permissions

from apps.users.models import User
from apps.users.serializers import UserSerializer

class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [permissions.AllowAny]