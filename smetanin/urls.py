from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from mainapp.views import *
from smetanin import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', start_page, name='start_page'),
    path('achievents/', achievements_page, name='achievements_page'),
    path('feedback/', feedback_page, name='feedback_page'),
    path('albums/', albums_page, name='albums_page'),
    path('photos/<int:albumid>/', photos_page, name='photos_page')
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
