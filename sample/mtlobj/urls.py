from django.urls import path,include
from .views import mtlbviewse
from rest_framework import routers
router = routers.DefaultRouter()
router.register("get",mtlbviewse)

urlpatterns = [
path("api/", include(router.urls)),

]