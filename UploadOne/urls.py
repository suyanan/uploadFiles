from django.conf.urls import url

from . import views

app_name = 'UploadOne'

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^simple_upload/$',views.simple_upload,name='simple_upload'),
    url(r'^model_form_upload/$', views.model_form_upload, name='model_form_upload'),
]
