from rest_framework import viewsets
from rest_framework.throttling import AnonRateThrottle

from .models import Achievement, Cat, User

from .serializers import AchievementSerializer, CatSerializer, UserSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer
    # Подключили класс AnonRateThrottle
    # Классы имеют более высокий приоритет
    # throttle_classes = (AnonRateThrottle,)
    throttle_scope = 'low_rate'  # Для всех единое ограничение

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer
