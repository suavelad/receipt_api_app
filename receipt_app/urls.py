from django.urls import path
from rest_framework.routers import DefaultRouter
from .apis import  ReceiptView

router = DefaultRouter()
urlpatterns = router.urls

urlpatterns += [

    path('create/receipt/',ReceiptView.as_view())


]