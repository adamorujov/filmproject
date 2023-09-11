from rest_framework.generics import (
    ListAPIView, RetrieveAPIView, CreateAPIView, 
    UpdateAPIView, DestroyAPIView, 
    ListCreateAPIView, RetrieveUpdateDestroyAPIView
)
from film.models import FilmModel, ActorModel
from film.api.serializers import (
    FilmSerializer, FilmCreateSerializer,
    ActorSerializer, ActorCreateSerializer
)


class FilmListAPIView(ListAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer

class FilmRetrieveAPIView(RetrieveAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    lookup_field = "pk"

class FilmCreateAPIView(CreateAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmCreateSerializer

class FilmUpdateAPIView(UpdateAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    lookup_field = "pk"

class FilmDestroyAPIView(DestroyAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    lookup_field = "pk"

class FilmRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = FilmModel.objects.all()
    serializer_class = FilmSerializer
    lookup_field = "pk"

class ActorListAPIView(ListAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer

class ActorRetrieveAPIView(RetrieveAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "pk"

class ActorCreateAPIView(CreateAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorCreateSerializer

class ActorUpdateAPIView(UpdateAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorCreateSerializer
    lookup_field = "pk"

class ActorDestroyAPIView(DestroyAPIView):
    queryset = ActorModel.objects.all()
    serializer_class = ActorSerializer
    lookup_field = "pk"