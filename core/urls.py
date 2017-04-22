from django.conf.urls import url

from core.views import IndexView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
]
