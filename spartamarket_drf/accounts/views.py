from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.


@api_view(["GET"])
def user_profile(request, username):

    permission_classes = [IsAuthenticated]
    if request.user.username == username:
        member = get_object_or_404(get_user_model(), username=username)
        serializer = UserSerializer(member)
        return Response(serializer.data)
    else:
        data = {"안돼 돌아가"}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
