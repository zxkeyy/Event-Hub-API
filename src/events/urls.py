from django.urls import path
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('events', views.EventViewSet)
router.register('clubs', views.ClubViewSet)
router.register('universities', views.universityViewSet)
router.register('categories', views.CategoryViewSet)

urlpatterns = router.urls