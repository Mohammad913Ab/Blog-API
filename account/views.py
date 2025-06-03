from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny
from rest_framework.generics import  CreateAPIView
from .serializer import UserSerializer




class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = UserSerializer