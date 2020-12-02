from django.urls import path, include
from django.conf.urls import url

from rest_framework.routers import DefaultRouter
from test import views

router = DefaultRouter()
router.register('viewset', views.TestViewSet, basename='test-viewset')
router.register('model-viewset', views.TestModelViewSet)
router.register('feed', views.TestFeedItemViewSet)



urlpatterns = [

    path("listProject/", views.ProjectList_EN_APIView.as_view(), name="list Project"),
    path("listProject/tr/", views.ProjectList_TR_APIView.as_view(), name="list Project"),
    path("listProject/UK/en/", views.ProjectList_UK_EN_APIView.as_view(), name="list Project"),
    path("listProject/UK/tr/", views.ProjectList_UK_TR_APIView.as_view(), name="list Project"),

    path("", include(router.urls))
]
