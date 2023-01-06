from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from .models import Location, Episode, Character
from .serializers import LocationSerializer, EpisodeSerializer, CharacterSerializer, CreateEpisodeSerializer
from .permissions import IsAuthenticated, IsOwner


class LocationModelViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer
    permission_classes = [IsOwner]

    def list(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            queryset = Location.objects.filter(author=request.user).exists()
            if queryset:
                queryset = Location.objects.filter(author=request.user)
                serializer = LocationSerializer(queryset, many=True)
                return Response(serializer.data)
            else:
                return Response({'message': 'У вас нет локаций'}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({'message': 'Вы не авторизованы'}, status=status.HTTP_401_UNAUTHORIZED)


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
