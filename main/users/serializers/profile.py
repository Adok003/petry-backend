from rest_framework import serializers
from ..models import CustomUser

class UserMeSerializer(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()
    head = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'region', 'role', 'head']

    def get_role(self, obj):
        return obj.role.name if obj.role else None

    def get_head(self, obj):
        return obj.head.email if obj.head else None
