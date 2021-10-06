from django.urls import path
from .views import XxxxxList, XxxxxDetail

urlpatterns = [
    path("", XxxxxList.as_view(), name="Xxxxx_list"),
    path("<int:pk>/", XxxxxDetail.as_view(), name="Xxxxx_detail"),
]
