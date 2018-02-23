from rest_framework import mixins, generics
from athletes.models import Athlete
from athletes.serializers import AthleteSerializer


class AthleteAPIView(generics.ListCreateAPIView):  # create view
    queryset = Athlete.objects.all()
    lookup_field = "pk"
    serializer_class = AthleteSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class AthleteRudView(generics.RetrieveUpdateDestroyAPIView):  # detail view
    lookup_field = "pk"
    serializer_class = AthleteSerializer

    def get_queryset(self):
        return Athlete.objects.all()