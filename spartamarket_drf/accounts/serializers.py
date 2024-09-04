from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","password", "nickname", "gender",
                  "birth_date", "email", "introduce"]
        read_only_fields = ()  # 읽기 전용으로 부름

    #이메일 중복 방지
    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("이 이메일은 이미 사용 중입니다.")
        return value
    
    # 비밀번호 해시화를 위해 create함수 오버라이딩
    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None :
            #provide django, password will be hashing!
            instance.set_password(password)
        instance.save()
        return instance
