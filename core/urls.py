from .views import DoctorViewSet, PatientViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'patients', PatientViewSet, basename='patient')
urlpatterns = router.urls