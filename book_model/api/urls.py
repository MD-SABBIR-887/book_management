from django.urls import path
from . import views


urlpatterns = [
    path('', views.BookViewSet.as_view({'get': 'list', 'post': 'create'}), name='booklist'),
    path ('<pk>/', views.BookViewSet.as_view({'get': 'retrieve', 'put': 'update', 'patch': 'partial_update', 'delete': 'destroy'}), name='bookdetails'),
    path('reviews/', views.ReviewListView.as_view(), name='reviewlist'),
    path ('reviews/<pk>/', views.ReviewDetailsView.as_view(), name='reviewdetail'),
]

# # book_model/urls.py
# from django.urls import path, include
# from rest_framework.routers import DefaultRouter
# from .views import BookViewSet

# router = DefaultRouter()
# router.register("books", BookViewSet)

# urlpatterns = [
#     path("", include(router.urls)),
# ]
