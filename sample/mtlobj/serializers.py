from rest_framework import serializers
from .models import mtlbobj
class objmtl(serializers.ModelSerializer):
    class Meta:
        model=mtlbobj
        fields='__all__'