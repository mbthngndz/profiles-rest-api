from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_422_UNPROCESSABLE_ENTITY

from profiles_api import permissions

from test.models import Test, TestFeedItem
from test.permissions import UpdateTestStatus
from test.serializers import TestModelSerializer, TestFeedItemSerializer

from django.db.models import Q


class TestViewSet(viewsets.ViewSet):
    serializer_class = TestModelSerializer

    def list(self, request):
        queryset = Test.objects.all()
        serializer = TestModelSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Test.objects.all()
        test = get_object_or_404(queryset, pk=pk)
        serializer = TestModelSerializer(test)
        return Response(serializer.data)


class TestModelViewSet(viewsets.ModelViewSet):
    serializer_class = TestModelSerializer
    queryset = Test.objects.all()

    # permission_classes = (permissions.UpdateOwnProfile,)

    # def perform_create(self, serializer):
    #    serializer.save() # parantezin içine first_name(modelin içinde verilen herhangi bir field olabilir)=self.request.user yazılırsa create eden user'ın adı otomatik gelir.


class TestFeedItemViewSet(viewsets.ModelViewSet):
    serializer_class = TestFeedItemSerializer
    queryset = TestFeedItem.objects.all()
    permission_classes = (UpdateTestStatus, IsAuthenticated)
    authentication_classes = (TokenAuthentication,)


class ProjectList_EN_APIView(ListAPIView):
    serializer_class = TestModelSerializer
    queryset = Test.objects.filter((Q(country="TR") | Q(country="Common")) & Q(language="English"))


class ProjectList_TR_APIView(ListAPIView):
    serializer_class = TestModelSerializer
    queryset = Test.objects.filter((Q(country="TR") | Q(country="Common")) & Q(language="Turkish"))


class ProjectList_UK_EN_APIView(ListAPIView):
    serializer_class = TestModelSerializer
    queryset = Test.objects.filter((Q(country="UK") | Q(country="Common")) & Q(language="English"))


class ProjectList_UK_TR_APIView(ListAPIView):
    serializer_class = TestModelSerializer
    queryset = Test.objects.filter((Q(country="UK") | Q(country="Common")) & Q(language="Turkish"))
