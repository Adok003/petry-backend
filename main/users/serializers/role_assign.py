from rest_framework import serializers
from ..models import CustomUser

class UserSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'role', 'head']
        read_only_fields = ['role', 'head']