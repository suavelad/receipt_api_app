from .serializers import ReceiptSerializer, CreateListMixin, ReceiptsSerializer,UserSerializer
from .schemas import ReceiptSchema
from .models import Receipts
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.response import Response
from django.db import connection
import collections
from rest_framework import status, views, permissions,generics
from rest_framework import serializers
from django.core.exceptions import ValidationError

from rest_framework.permissions import AllowAny
from rest_framework.generics import CreateAPIView, ListCreateAPIView
from rest_framework.mixins import CreateModelMixin
from rest_framework_bulk import  ListBulkCreateUpdateDestroyAPIView



class ReceiptView(ListBulkCreateUpdateDestroyAPIView):
    schema =ReceiptSchema
    queryset = Receipts.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticated,)
    


 


