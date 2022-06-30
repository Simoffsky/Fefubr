from rest_framework import generics
from .models import *
from .serializers import *


class SubscribeListView(generics.ListCreateAPIView):
    serializer_class = UserSubscriptionSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        if pk is None:
            return UserSubscribtion.objects.all()  # Стоит ли бросать ошибку?
        return UserSubscribtion.objects.filter(user_id=pk)


