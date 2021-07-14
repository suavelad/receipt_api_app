from rest_framework.viewsets import ModelViewSet
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Company
from .schemas import LoginSchema
from .serializers import CompanySerializer, SIDSerializer, EmployeeSerializer, ReceptionistSerializer, GateStaffSerializer, GroupSerializer, LoginSerializer
from .permissions import IsSIDPermission

class CompanyViewSet(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [IsSIDPermission]

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


class GroupViewSet(ModelViewSet):
    """
    list:
    Retuns a list of all group
    
    create:
    Create a new group

    retrieve:
    Return the group with the given id

    update:
    Update (full) group info with the given id

    partial_update:
    Update (partial) group info with the given id

    delete:
    Delete group with the given id
    """
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

class SIDViewSet(ModelViewSet):
    """
    list:
    Retuns a list of all sid
    
    create:
    Create a new sid

    retrieve:
    Return the sid with the given id

    update:
    Update (full) sid info with the given id

    partial_update:
    Update (partial) sid info with the given id

    delete:
    Delete sid with the given id
    """
    def get_queryset(self):
        return get_user_model().objects.filter(groups__name='sid')
    serializer_class = SIDSerializer   

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


class ReceptionistViewSet(ModelViewSet):
    """
    list:
    Retuns a list of all receptionist
    
    create:
    Create a new receptionist

    retrieve:
    Return the receptionist with the given id

    update:
    Update (full) receptionist info with the given id

    partial_update:
    Update (partial) receptionist info with the given id

    delete:
    Delete receptionist with the given id
    """
    def get_queryset(self):
        return get_user_model().objects.filter(groups__name='rec')
    serializer_class = ReceptionistSerializer

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
    

class EmployeeViewSet(ModelViewSet):
    """
    list:
    Retuns a list of all employee
    
    create:
    Create a new employee

    retrieve:
    Return the employee with the given employee

    update:
    Update (full) employee info with the given employee

    partial_update:
    Update (partial) employee info with the given employee

    delete:
    Delete employee with the given employee
    """
    def get_queryset(self):
        return get_user_model().objects.filter(groups__name='emp')
    serializer_class = EmployeeSerializer

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


class GateStaffViewSet(ModelViewSet):
    """
    list:
    Retuns a list of all gate-staff
    
    create:
    Create a new gate-staff

    retrieve:
    Return the gate-staff with the given id

    update:
    Update (full) gate-staff info with the given id

    partial_update:
    Update (partial) gate-staff info with the given id

    delete:
    Delete gate-staff with the given id
    """
    def get_queryset(self):
        return get_user_model().objects.filter(groups__name='gat')
    serializer_class = GateStaffSerializer

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
        try:
            key = request.headers['App-Id']
            try:
                company = Company.objects.get(app_key=key)
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
            except Company.DoesNotExist:
                return Response({
                    "code": 130,
                    "message": "Company does not exist",
                    "resolve": "Your app id does not exist"
                },status=status.HTTP_404_NOT_FOUND)
        except KeyError:
            return Response({
                    "code": 140,
                    "message": "App Id not included in the header",
                    "resolve": "Add the id with the keyword App-Id"
                },status=status.HTTP_404_NOT_FOUND)
