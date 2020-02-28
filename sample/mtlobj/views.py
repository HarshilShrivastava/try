from django.shortcuts import render
from .models import mtlbobj
from .serializers import objmtl
from rest_framework import viewsets
from rest_framework.response import Response
class mtlbviewse(viewsets.ModelViewSet):
    queryset = mtlbobj.objects.all()
    serializer_class = objmtl
    

    def list(self, request, *args, **kwargs):
        self.object_list = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(self.object_list, many=True)
        return Response({'data': serializer.data})