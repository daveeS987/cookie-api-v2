from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie_Stand
from .permissions import IsOwnerOrReadOnly
from .serializers import Cookie_StandSerializer


class Cookie_StandList(ListCreateAPIView):
    queryset = Cookie_Stand.objects.all()
    serializer_class = Cookie_StandSerializer


class Cookie_StandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookie_Stand.objects.all()
    serializer_class = Cookie_StandSerializer
