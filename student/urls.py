from django.urls import path, include
from rest_framework import routers
from .views import CourseViewSet, StudentViewSet

router = routers.DefaultRouter()
router.register('course', CourseViewSet)
router.register('student', StudentViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]

