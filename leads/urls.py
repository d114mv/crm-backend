from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CarreraViewSet, LeadViewSet, InteraccionViewSet

router = DefaultRouter()
router.register(r'carreras', CarreraViewSet)
router.register(r'leads', LeadViewSet)
router.register(r'interacciones', InteraccionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]