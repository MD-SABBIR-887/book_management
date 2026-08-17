from django.db.migrations import serializer
from django.shortcuts import render
from book_model.models import BookList, Review
from . import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import permission_classes, throttle_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.shortcuts import get_object_or_404
from rest_framework.throttling import AnonRateThrottle, UserRateThrottle
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from .serializers import BookListSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class BookViewSet(viewsets.ModelViewSet):
    queryset = BookList.objects.all().order_by("id")
    serializer_class = BookListSerializer
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["category", "author"]
    search_fields = ["category", "author"]
    ordering_fields = ["id", "price"]
    ordering = ["id"]
    def get(self, request):
        books = BookList.objects.all().order_by("id")
        paginator = PageNumberPagination()
        page = paginator.paginate_queryset(queryset=books, request=request)
        serializer = serializers.BookListSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = serializers.BookListSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




    
    
class BookDetailsView(APIView):
    queryset = BookList.objects.all().order_by("id")
    permission_classes = [IsAuthenticated]
    serializer_class = BookListSerializer
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'author']
    search_fields = ["category", "author"]
    ordering_fields = ["id", "price"]
    ordering = ["id"]
    
    def get(self, request, pk):
        book = get_object_or_404(BookList, pk=pk)
        queryset = BookList.objects.all().order_by("id")
        serializer = serializers.BookListSerializer(book, queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        book = get_object_or_404(BookList, pk=pk)
        serializer = serializers.BookListSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        book = get_object_or_404(BookList, pk=pk)
        serializer = serializers.BookListSerializer(book, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        book = get_object_or_404(BookList, pk=pk)
        book.delete()
        return Response({"message": "Book deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
    
    
class ReviewListView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    def get(self, request):
        review = Review.objects.all()
        serializer = serializers.ReviewSerializer(review, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        data = request.data
        serializer = serializers.ReviewSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    
    
class ReviewDetailsView(APIView):
    permission_classes = [IsAuthenticated]
    throttle_classes = [AnonRateThrottle, UserRateThrottle]
    
    
    def get(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = serializers.ReviewSerializer(review)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def put(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = serializers.ReviewSerializer(review, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def patch(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        serializer = serializers.ReviewSerializer(review, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):
        review = get_object_or_404(Review, pk=pk)
        review.delete()
        return Response({"message": "Review deleted successfully."}, status=status.HTTP_204_NO_CONTENT)












