from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    # Page d'accueil simple
    path('', TemplateView.as_view(template_name='home.html'), name='home'),

    # Inclusion des apps
    path('accounts/', include('accounts.urls')),
    path('courses/', include('courses.urls')),
    path('grades/', include('grades.urls')),
    path('goals/', include('goals.urls')),
]

# Configuration pour servir les fichiers média en dev
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)