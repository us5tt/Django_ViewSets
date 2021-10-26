from django.shortcuts import render
from rest_framework import viewsets
from django.http import HttpResponse

from .models import Pars
from .serializers import ParsSerializer


def index(request):
    return render (request, "api/index.html")


class ParsView(viewsets.ModelViewSet):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer


class SingleParsView(viewsets.ModelViewSet):
    queryset = Pars.objects.all()
    serializer_class = ParsSerializer

