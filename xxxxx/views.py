from rest_framework import generics
from .serializers import XxxxxSerializer
from .models import Xxxxx
from .permissions import IsOwnerOrReadOnly


class XxxxxList(generics.ListCreateAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Xxxxx.objects.all()
    serializer_class = XxxxxSerializer


class XxxxxDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Xxxxx.objects.all()
    serializer_class = XxxxxSerializer
