from django.urls import path
from rest_framework.routers import DefaultRouter
from .apis import  ReceiptView

router = DefaultRouter()
# router.register('create/receipt',CreateReceiptView)
urlpatterns = router.urls

urlpatterns += [
    # path('generate/receipt/', GenReceiptsView.as_view(), name='generate_receipt'),
    # path('create/receipt/',CreateReceiptView.as_view())
    path('create/receipt/',ReceiptView.as_view())


    



]