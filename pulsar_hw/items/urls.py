from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import ItemViewSet

router = DefaultRouter()
router.register(r'items', ItemViewSet, basename='items')

urlpatterns = [
    path('', include(router.urls))
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
