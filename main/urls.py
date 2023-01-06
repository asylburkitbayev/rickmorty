from rest_framework.routers import DefaultRouter
from .views import LocationModelViewSet, EpisodeModelViewSet, CharacterModelViewSet

routers = DefaultRouter()

routers.register('location', LocationModelViewSet)
routers.register('episode', EpisodeModelViewSet)
routers.register('character', CharacterModelViewSet)

urlpatterns = routers.urls
