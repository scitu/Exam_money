from rest_framework import viewsets
from exam.serializers import LacSerializer
from exam.models import Lac

class LacViewSet(viewsets.ModelViewSet):
    queryset = Lac.objects.all()
    serializer_class = LacSerializer
