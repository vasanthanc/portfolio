from django.urls import include, path
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404

# handler404 = views.render_contact_page
urlpatterns = [
    path('contact', views.render_contact_page, name='contact'),
    path('', views.HomePageView.as_view(), name='index'),
    path('index', views.HomePageView.as_view(), name='index'),
    path('about', views.AboutMePageView.as_view(), name='about'),
    path('submitform',views.send_mail_local, name='submit')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)