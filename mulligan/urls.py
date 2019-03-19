from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url("get_hand",views.get_hand),
]
