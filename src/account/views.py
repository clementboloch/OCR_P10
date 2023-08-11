from rest_framework.views import APIView
from .serializers import RegisterSerializer
from rest_framework.response import Response

from datetime import date


# view for registering users
class RegisterView(APIView):
    def post(self, request):
        data = request.data
        data._mutable = True
        birthdate = data.get('birthdate')
        birthdate = date.fromisoformat(birthdate)
        today = date.today()
        age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

        if age < 15:
            data['can_be_contacted'] = False
            data['can_data_be_shared'] = False

        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
