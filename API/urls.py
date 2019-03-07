from django.urls import include, path
from rest_framework import routers
from API import views

router = routers.DefaultRouter()
router.register('posts', views.PostViewSet, base_name="posts")




urlpatterns = [
    path('', include(router.urls), name='router_posts'),
]