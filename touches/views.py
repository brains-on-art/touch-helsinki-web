from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Delta


class DeltaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delta
        fields = ['ts', 'lattice']


@method_decorator(csrf_exempt, name='dispatch')
class DeltaView(APIView):
    @csrf_exempt
    def post(self, request, format=None):
        # print(request.data)
        serializer = DeltaSerializer(data=request.data)

        if serializer.is_valid() and serializer.validated_data['lattice']:
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        print(request)
        feedbacks = Delta.objects.all()
        serializer = DeltaSerializer(feedbacks, many=True)
        return Response(serializer.data)
