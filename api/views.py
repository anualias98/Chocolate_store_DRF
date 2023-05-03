from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.renderers import TemplateHTMLRenderer, JSONRenderer
from rest_framework.response import Response
from .serializers import ChocoSerializer
from .models import Chocolate


# Create your views here.


class ListChocolate(generics.ListCreateAPIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'list.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def list(self, request):
        queryset = self.get_queryset()
        return Response({'object_list': queryset})


class DetailChoco(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'detail.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        return Response({'object': queryset})


class ChocoCheckoutView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'checkout.html'
    queryset = Chocolate.objects.all()
    serializer_class = ChocoSerializer

    def get(self, request, *args, **kwargs):
        queryset = self.get_object()
        return Response({'object': queryset})


def home(request):
    return render(request, 'home.html')
