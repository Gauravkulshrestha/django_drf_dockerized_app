from rest_framework.viewsets import ModelViewSet
from .models import ToDo
from .serializers import ToDoSerializer

class ToDoView(ModelViewSet):
    queryset = ToDo.objects.all()
    serializer_class = ToDoSerializer