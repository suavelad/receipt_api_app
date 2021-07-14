from django.urls import path
from rest_framework.routers import DefaultRouter
from .apis import CashierViewSet, GroupViewSet, AdminViewSet,  LoginView

router = DefaultRouter()

router.register('groups', GroupViewSet)
router.register('admin', AdminViewSet, 'adm')
router.register('cashier', CashierViewSet, 'cashier')

urlpatterns = router.urls

urlpatterns += [
    path('login/', LoginView.as_view(), name='login'),
]