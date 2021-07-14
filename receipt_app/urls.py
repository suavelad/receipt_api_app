from django.urls import path
from rest_framework.routers import DefaultRouter
from .apis import GenReceiptsView,ReceiptViewSet

router = DefaultRouter()
router.register('create/receipt',ReceiptViewSet)
urlpatterns = router.urls

urlpatterns += [
    path('generate/receipt/', GenReceiptsView.as_view(), name='generate_receipt'),


]