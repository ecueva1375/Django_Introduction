from django.urls import path, include
from . import views
# from .views import Another
from rest_framework import routers
from .views import BookVieSet

router = routers.DefaultRouter()
router.register('books', BookVieSet)

urlpatterns = [
    #path('', views.first)
    path('', include(router.urls))
    # path('another', Another.as_view())
]