from rest_framework import routers
from exam.viewsets import LacViewSet

router = routers.DefaultRouter()
router.register(r'Lac', LacViewSet)
