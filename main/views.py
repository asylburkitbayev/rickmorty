from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Location, Episode, Character
from .serializers import LocationSerializer, EpisodeSerializer, CharacterSerializer, CreateEpisodeSerializer


class LocationModelViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer


class EpisodeModelViewSet(ModelViewSet):
    queryset = Episode.objects.all()
    serializer_class = CreateEpisodeSerializer

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = EpisodeSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = EpisodeSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = EpisodeSerializer(instance)
        return Response(serializer.data)


class CharacterModelViewSet(ModelViewSet):
    queryset = Character.objects.all()
    serializer_class = CharacterSerializer
