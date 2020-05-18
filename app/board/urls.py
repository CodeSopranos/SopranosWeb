from django.urls import path
from . import views


urlpatterns = [
    path('', views.dashboard),
    path('parse_theme', views.parse_theme),
    # path('<int:dashboard_id>/parse_theme', views.parse_theme, name='parse_theme')
]
