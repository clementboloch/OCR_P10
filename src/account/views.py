from rest_framework.views import APIView
from rest_framework import generics
from .serializers import RegisterSerializer, UpdateSerializer
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from datetime import date

from .models import UserData


def verify_age(data):
    data._mutable = True
    birthdate = data.get('birthdate')
    birthdate = date.fromisoformat(birthdate)
    today = date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    if age < 15:
        data['can_be_contacted'] = False
        data['can_data_be_shared'] = False

    return data


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        data = verify_age(data)

        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


# view for listing and updating user data
class ListUpdateView(generics.RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)

    queryset = UserData.objects.all()
    serializer_class = UpdateSerializer

    def get_object(self):
        return self.request.user

    def put(self, request):
        data = request.data
        data = verify_age(data)
        return super().put(request)
