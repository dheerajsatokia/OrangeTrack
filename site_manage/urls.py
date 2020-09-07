from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

router = routers.SimpleRouter(trailing_slash=False)
router.register(r'site', views.SiteViewSet)

urlpatterns = [
]
urlpatterns += format_suffix_patterns(router.urls)