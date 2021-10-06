from rest_framework import serializers
from .models import Cookie_Stand


class Cookie_StandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cookie_Stand
        fields = "__all__"
