from django.conf.urls import url,include

from . import views

app_name='twit_app'

urlpatterns = [
    #url(r'^$', views.index,name='index'),
    #url(r'^new/', views.form_data, name='new'),
    url(r'^form_data/$', views.form_data),
]
