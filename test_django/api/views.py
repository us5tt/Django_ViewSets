from rest_framework import viewsets
from django.http import HttpResponse

from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return HttpResponse("main page coming soon")


class ParsView(viewsets.ModelViewSet):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(viewsets.ModelViewSet):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer

