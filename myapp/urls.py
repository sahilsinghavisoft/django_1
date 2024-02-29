from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import employeeviewset,companyviewset

router = DefaultRouter()
router.register(r'employee', employeeviewset)
router.register(r'company',companyviewset)

urlpatterns = [
    path('', include(router.urls)),
    # other URL patterns if any
    
]
