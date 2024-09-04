

from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer, ProductDetailSerializer

# 읽기 전용으로 가져올거면


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class ProductListAPIView(APIView):

    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        # return Response(serializer.errors, status=400)을 대신함
        if serializer.is_valid(raise_exception=True):
            serializer.save(author=request.user)
            # 201은 created
            return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetailAPIView(APIView):

    permission_classes = [IsAuthenticated | ReadOnly]

    # 자주 쓰는 함수는 요렇게 따로 정의
    def get_object(self, pk):
        return get_object_or_404(Product, pk=pk)

    def put(self, request, productId):
        product = self.get_object(productId)
        if product.author == request.user:
            serializer = ProductDetailSerializer(
                product, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)
        else:
            return Response({"message": "작성자가 아닙니다. 수정불가"}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, productId):
        product = self.get_object(productId)
        if product.author == request.user:
            product.delete()
            # 204는 삭제
            return Response({"message": "삭제 되었습니다~"}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"message": "작성자가 아닙니다. 삭제불가"}, status=status.HTTP_403_FORBIDDEN)
