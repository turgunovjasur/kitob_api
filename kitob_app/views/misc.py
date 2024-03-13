from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from kitob_app.models import Order
from kitob_app.models import Review, Category
from kitob_app.permissions import IsOwnerOrReadOnly
from kitob_app.serializers import OrderSerializer
from kitob_app.serializers import ReviewSerializer, CategorySerializer


class OrderViewSet(viewsets.ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  # default =  AllowAny

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

