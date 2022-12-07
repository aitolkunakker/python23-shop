from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from  rest_framework.decorators import api_view



from .serializers import RegisterUserSerializer
from .models import User

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=RegisterUserSerializer)
    def post(self,request):
        serializer = RegisterUserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response('вы успешно зарегистрировались', status=201)

