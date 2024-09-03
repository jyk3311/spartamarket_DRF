from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ()  # 읽기 전용으로 부름

    # def to_representation(self, instance):  # 보여주는 함수 오버라이딩
    #     ret = super().to_representation(instance)
    #     ret.pop("id", 'password', "last_login", "is_superuser", "is_staff", "is_active",
    #             "date_joined", "groups", "user_permissions")  # forms에 except같은 것
    #     return ret
