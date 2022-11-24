from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from bookshop.models import Book, Author
from rest_framework.generics import ListCreateAPIView
from rest_framework.views import APIView
from .serializers import BookSerializer
from rest_framework import viewsets


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated, )

# class BookAPIList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer

# class BookAPIView(APIView):
#     def get(self, request):
#         books = Book.objects.all()
#         return Response({'books': BookSerializer(books, many=True).data})
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({'book': serializer.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method PUT not allowed"})
#         try:
#             instance = Book.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#         serializer = BookSerializer(data=request.data, instance=instance)
#         serializer.is_valid()
#         serializer.save()
#         return Response({"book": serializer.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#         try:
#             instance = Book.objects.get(pk=pk)
#         except:
#             return Response({"error": "Object does not exist"})
#         return Response({'book':'delete post ' + str(pk) })
