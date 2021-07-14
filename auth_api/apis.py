from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .schemas import LoginSchema
from .serializers import AdminSerializer,CashierSerializer, GroupSerializer, LoginSerializer


class GroupViewSet(ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def create(self, request, args, *kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'Successful'
            }, status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)

class AdminViewSet(ModelViewSet):
 
    def get_queryset(self):
        return get_user_model().objects.filter(groups__name='adm')
    serializer_class = AdminSerializer   

    def create(self, request, args, *kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'Successful'
            }, status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)

class CashierViewSet(ModelViewSet):

    def get_queryset(self):
        return get_user_model().objects.filter(groups__name='csh')
    serializer_class = CashierSerializer

    def create(self, request, args, *kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': 'Successful'
            }, status=status.HTTP_201_CREATED)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    schema = LoginSchema

    def post(self, request):    
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data["email"]
            password = serializer.validated_data['password']
            try:
                user = User.objects.get(email=email)
                if user.check_password(password):
                    if user.is_active:
                        login(request, user)
                        return Response(LoginSerializer(user).data, status=status.HTTP_200_OK)
                    else:
                        return Response({
                            "code": 110,
                            "message": "unverified account",
                            "resolve": "please verify your account"
                        }, status=status.HTTP_401_UNAUTHORIZED)
                else:
                    return Response({
                    "code": 120,
                    "message": "incorect password",
                    "resolve": "The password does not match with the email"
                }, status=status.HTTP_401_UNAUTHORIZED)
            except User.DoesNotExist:
                return Response({
                    "code": 120,
                    "message": "user does not exist",
                    "resolve": "There's no account matching this email"
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)
