from django.conf.urls import url
from . import views

urlpatterns = [
		url(r'^$', views.index, name='index'),
    url(r'^schedule_meeting/', views.schedule_meeting, name='schedule_meeting'),
    url(r'^get_future_meetings/', views.get_future_meetings, name='get_future_meetings'),
]