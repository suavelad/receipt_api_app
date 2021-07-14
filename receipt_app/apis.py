from .serializers import ReceiptSerializer, CreateListMixin
from .schemas import ReceiptSchema
from .models import Receipts
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from django.db import connection
import collections
from rest_framework import status, views, permissions


class ReceiptViewSet(ModelViewSet,CreateListMixin):
    queryset = Receipts.objects.all()
    serializer_class = ReceiptSerializer
    permission_classes = (permissions.IsAuthenticated,)


class generate_receipt(object):
    @staticmethod
    def get_data(user_id, start_date, end_date):
        cur = connection.cursor()
        cur.callproc('generate_receipt',[user_id, start_date, end_date])
        rows = cur.fetchall()
        print(rows)
        field_names = [i[0] for i in cur.description]
        objects_list = []
        for row in rows:
            d = collections.OrderedDict()
            d[field_names[0]] = row[0]
            d[field_names[1]] = row[1]
            d[field_names[2]] = row[2]
            d[field_names[3]] = row[3]
            d[field_names[4]] = row[4]
            d[field_names[5]] = row[5]
            d[field_names[6]] = row[6]
            d[field_names[7]] = row[7]
            d[field_names[8]] = row[8]
            d[field_names[9]] = row[9]
            d[field_names[10]] = row[10]
            d[field_names[11]] = row[11]

            objects_list.append(d)
        print('>>>>>>>', objects_list)
        cur.close()
        return objects_list

class GenReceiptsView(views.APIView):
    schema = ReceiptSchema
    def post(self, request):
        serializer = ReceiptSerializer(data=request.data)
        if serializer.is_valid():
            total = generate_receipt.get_data(
                cashier_user= serializer.validated_data['cashier_user'],
                customer_name=serializer.validated_data['customer_name'],
                customer_phone=serializer.validated_data['customer_phone'],
                customer_address = serializer.validated_data['customer_address'] ,
                item = serializer.validated_data['item'] ,
                unit_price = serializer.validated_data['unit_price'] ,
                quantity = serializer.validated_data['quantity'] ,
                total = unit_price * quantity,
                description = serializer.validated_data['description'] 
            )

            if total is None or total == []:
                return Response(
                    {'code': 141,
                     'message': 'Invalid data',
                     'resolve': 'Check the inserted field'}
                    )
            else:
                return Response({
                    'status': 200,
                    'result': total
                }, status=status.HTTP_200_OK)
        else:
            return Response(serializer.custom_full_errors, status=status.HTTP_400_BAD_REQUEST)