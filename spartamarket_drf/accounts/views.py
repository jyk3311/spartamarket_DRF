from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.contrib.auth import get_user_model
from .serializers import UserSerializer
# Create your views here.


@api_view(["GET", "POST"])
# 회원가입
# Endpoint : /api/accounts
# Method : POST
# 조건 : username, 비밀번호, 이메일, 이름, 닉네임, 생일 필수 입력하며 성별, 자기소개 생략 가능
# 검증 : username과 이메일은 유일해야 하며, 이메일 중복 검증(선택 기능).
# 구현 : 데이터 검증 후 저장.
def sign_up(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)  # 요청 데이터로 Serializer 생성
        if serializer.is_valid(raise_exception=True):  # 데이터가 유효한지 검사
            user = serializer.save()
            return Response({"message": "회원가입이 성공적으로 완료되었습니다.", "user_id": user.id}, serializer.data,
                            status=status.HTTP_201_CREATED)


# 프로필 조회
# Endpoint : /api/accounts/<str:username>
# Method : GET
# 조건 : 로그인 상태 필요.
# 검증 : 로그인 한 사용자만 프로필 조회 가능
# 구현 : 로그인한 사용자의 정보를 JSON 형태로 반환.
@api_view(["GET"])
def user_profile(request, username):
    # 인증된 사용자만 접근 가능
    permission_classes = [IsAuthenticated]

    # 데이터베이스 찾아봤는데 없으면 404처리
    member = get_object_or_404(get_user_model(), username=username)

    if request.user.username == username:  # 로그인한 유저가 자기 프로필로 접근하는지 확인
        serializer = UserSerializer(member)
        return Response(serializer.data, status=status.HTTP_200_OK)
    else:
        data = {"안돼 돌아가"}
        return Response(data, status=status.HTTP_403_FORBIDDEN)
