from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "nickname", "gender",
                  "birth_date", "email", "introduce"]
        read_only_fields = ()  # 읽기 전용으로 부름
