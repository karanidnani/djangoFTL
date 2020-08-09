from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, ActivityPeriod
from .serializer import UserSerializer
from .serializertime import TimeSerializer

class UserList(APIView):
    def get(self, request):
        #User = User.objects.all(), Model and local variable name can't be same -> referenced before assignment
        Userr = User.objects.all()
        serializer = UserSerializer(Userr, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class TimeList(APIView):
    def get(self, request):
        Timee = ActivityPeriod.objects.all()
        serializer = TimeSerializer(Timee, many=True)
        return Response(serializer.data)
    
    def post(self):
        pass